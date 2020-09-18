import flask
import os
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import random

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
    
    food_items = ["ramen", "dosas", "french baguette", "dumplings", "pesto pasta", "paneer", "rice"]
    random_num = random.randint(0, len(food_items) - 1)
    
    for tweet in auth_api.search(q=food_items[random_num], lang="en", result_type="recent"):
        user = tweet.user.name
        tweets = tweet.text
        
 
    return flask.render_template("index.html", u = user, t = tweets)
  
 

app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP', '0.0.0.0')
)