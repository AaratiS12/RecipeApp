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
    
    food_items = ["ramen", "dosa", "burrito", "dumplings", "pesto pasta", "paneer", "quesadillas"]
    random_num = random.randint(0, len(food_items) - 1)
    item = food_items[random_num]
   
    for tweet in auth_api.search(q=item, lang="en", result_type="popular", count = 1):
        user = tweet.user.name
        tweets = tweet.text
    print(tweet)
    spoonacular_key = os.environ['spoonacular_auth_key']  
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + spoonacular_key+"&query=" + item +"&number=1"
    response = requests.get(url)
    json_response = response.json()
    print(json_response)
    
    #image_food = json_response['results'][0]['image']
    image_food = "https://spoonacular.com/recipeImages/636830-312x231.jpg"
    return flask.render_template("index.html", u = user, t = tweets, image= image_food, item = item)

app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0')
)
