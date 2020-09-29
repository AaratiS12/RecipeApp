import flask
import os
from tweepy import OAuthHandler
from tweepy import API
from datetime import datetime, date, time, timedelta
import sys
import random
import requests
import json
from flask import Flask, render_template, request

app = flask.Flask(__name__)

def randomItem():
    food_items = ["pumpkin", "apple pie", "squash", "sweet potato", "corn", "soup", "cranberry"]
    random_num = random.randint(0, len(food_items) - 1)
    return(food_items[random_num])
    
    
def twitter(consumer_key, consumer_secret, access_token, access_token_secret, item):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)
    return(auth_api.search(q=item, lang="en", result_type="popular"))
    
    
def spoonacular(spoonacular_key, item):
    url_image = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + spoonacular_key+"&query=" + item
    response = requests.get(url_image)
    return(response.json())
    
    
@app.route('/')
def index():
    '''Environmental variables'''
    consumer_key= os.environ['consumer_key']
    consumer_secret= os.environ['consumer_secret']
    access_token= os.environ['access_token']
    access_token_secret= os.environ['access_token_secret']
    spoonacular_key = os.environ['spoonacular_auth_key']  
    
    
    '''Random Item'''
    item = randomItem()
    print(item)
    
    
    '''Processing for Twitter'''
    search = twitter(consumer_key, consumer_secret, access_token,access_token_secret, item)
    random_num_tweet = random.randint(0, len(search)-1)
    if search:
        tweet = search[random_num_tweet] 
        author = tweet.user.name
        tweets = tweet.text
        date = tweet.created_at
        d = date.date().strftime('%A %d %B %Y')
        time = date.strftime("%I:%M %p")
    else:
        author = "no author"
        tweets = "Tweet Error- no tweet found"
        d = "no date" 
        time = "no time"
    
    
    '''Processing for Spoonacular'''
    json_response = spoonacular(spoonacular_key, item)
    random_num_recipe = random.randint(0, len(json_response)-1)
    recipe_id = json_response['results'][random_num_recipe]['id']
    image_food = json_response['results'][random_num_recipe]['image']
    recipe_title = json_response['results'][random_num_recipe]['title']
    url_image_ingredients = "https://api.spoonacular.com/recipes/"+ str(recipe_id)+ "/information?apiKey=" + spoonacular_key
    response_ingredients = requests.get(url_image_ingredients)
    json_response_ingredient = response_ingredients.json()
    servings = json_response_ingredient["servings"]
    prep_time = json_response_ingredient["readyInMinutes"]
    src_url = json_response_ingredient["sourceUrl"]
    ingredient_list = []
    for ingredient in json_response_ingredient["extendedIngredients"]:
        ingredient_list.append(ingredient["original"])
    
    
    '''Sending data to HTML'''
    return flask.render_template(
        "main_index.html", author = author, tweet = tweets, date = d, time = time, image= image_food,
        recipe_title = recipe_title, servings= servings, prep_time = prep_time, 
        src_url=src_url, ingredient_list = ingredient_list)
    
app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0')
)
