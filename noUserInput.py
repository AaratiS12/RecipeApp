import flask
import os
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import random
import requests
import json
from flask import Flask, render_template, request

app = flask.Flask(__name__)

@app.route('/') #Python decorater
def index():
    consumer_key= os.environ['consumer_key']
    consumer_secret= os.environ['consumer_secret']
    access_token= os.environ['access_token']
    access_token_secret= os.environ['access_token_secret']
    spoonacular_key = os.environ['spoonacular_auth_key']  
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)
    
    food_items = ["pumpkin pie", "apple cider", "spaghetti squash", "sweet potato", "corn", "soup", "cranberry"]
    random_num = random.randint(0, len(food_items) - 1)
    item = food_items[5]
    
    '''Processing for Twitter'''
    for tweet in auth_api.search(q=item, lang="en", result_type="recent", count = 1):
        author = tweet.user.name
        tweets = tweet.text
        date = tweet.created_at
    
    '''Processing for Spoonacular'''
    url_image = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + spoonacular_key+"&query=" + item +"&number=1"
    response = requests.get(url_image)
    json_response = response.json()
    d = date.date().strftime('%A %d %B %Y')
    time = date.strftime("%I:%M %p")
    recipe_id = json_response['results'][0]['id']
    #image_food = json_response['results'][0]['image']
    recipe_title = json_response['results'][0]['title']
    #Hardcoded Image link for testing
    image_food = "https://spoonacular.com/recipeImages/636830-312x231.jpg"
    
    url_image_ingredients = "https://api.spoonacular.com/recipes/"+ str(recipe_id)+ "/information?apiKey=" + spoonacular_key
    response_ingredients = requests.get(url_image_ingredients)
    json_response_ingredient = response_ingredients.json()
    servings = json_response_ingredient["servings"]
    prep_time = json_response_ingredient["readyInMinutes"]
    src_url = json_response_ingredient["sourceUrl"]
    ingredient_list = []
    for ingredient in json_response_ingredient["extendedIngredients"]:
        ingredient_list.append(ingredient["original"])
    
    
    return flask.render_template(
        "main_index.html", author = author, tweet = tweets, date = d, time = time, image= image_food,
        recipe_title = recipe_title, servings= servings, prep_time = prep_time, 
        src_url=src_url, ingredient_list = ingredient_list)
    
    
    
app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0')
)
