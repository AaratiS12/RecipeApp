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
from flask import Flask, render_template, request, redirect, url_for

app = flask.Flask(__name__)

@app.route('/') #Python decorater
def index():
    return flask.render_template("input.html")
    
   
@app.route('/', methods=['POST'])
def my_form_post():
    
    consumer_key= os.environ['consumer_key']
    consumer_secret= os.environ['consumer_secret']
    access_token= os.environ['access_token']
    access_token_secret= os.environ['access_token_secret']
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)
    
    food_items = ["ramen", "dosa", "burrito", "dumplings", "pesto pasta", "paneer", "quesadillas"]
    random_num = random.randint(0, len(food_items) - 1)
    #item = food_items[random_num]
    item = request.form['text']
    
    for tweet in auth_api.search(q=item, lang="en", result_type="popular", count = 1):
        author = tweet.user.name
        tweets = tweet.text
        date = tweet.created_at
    
    spoonacular_key = os.environ['spoonacular_auth_key']  
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + spoonacular_key+"&query=" + item +"&number=1"
    response = requests.get(url)
    json_response = response.json()
    d = date.date().strftime('%A %d %B %Y')
    time = date.strftime("%I:%M %p")
    
    image_food = json_response['results'][0]['image']
    #image_food = "https://spoonacular.com/recipeImages/636830-312x231.jpg"
    return flask.render_template("main_index.html", author = author, tweet = tweets, date = d, time = time, image= image_food, item = item)
    

app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0')
)
