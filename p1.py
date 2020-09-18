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

app = flask.Flask(__name__)

@app.route('/') #Python decorater
def index():
    
    consumer_key= os.environ['consumer_key']
    consumer_secret= os.environ['consumer_secret']
    access_token= os.environ['access_token']
    access_token_secret= os.environ['access_token_secret']
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)
    
    food_items = ["ramen", "dosas", "french baguette", "dumpling", "pesto pasta", "paneer", "rice"]
    random_num = random.randint(0, len(food_items) - 1)
    print(random_num)
    for tweet in auth_api.search(q=food_items[random_num], lang="en", result_type="popular"):
        user = tweet.user.name
        tweets = tweet.text
        
    spoonacular_key = os.environ['spoonacular_auth_key']  
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + spoonacular_key+"&query=" + food_items[random_num] +"&number=1"
    response = requests.get(url)
    json_response = response.json()
    print(json_response)
    
    image_food = json_response['results'][0]['image']
    return flask.render_template("index.html", u = user, t = tweets, image= image_food)

app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0')
)
