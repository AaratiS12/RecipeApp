# project1-as3243
A web application that collects tweets using Tweepy and displays relevant images from Spoonacular using the Spoonacular API. on my favorite foods
This is a simple demo of Heroku using the Twitter API.

To use this repository, you must follow these steps:
0. Sign up for the twitter developer portal at https://developer.twitter.com
1. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
2. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
    If needed, you can regenerate your access token and secret.
3. Sign up for the spoonacular account at https://spoonacular.com/food-api. Navigate to my console, then profile and copy your hidden keys.
4. Clone this repository by using git clone https://github.com/NJIT-CS490/project1-as3243
5. Run the following in your terminal:
    sudo pip install tweepy
    (or) sudo pip3 install tweepy
    (or) pip install tweepy
    (or) pip3 install tweepy
6. Install flask using the same process as above ([sudo] pip[3] install flask)
7. Install requests using the same process as above ([sudo] pip[3] install requests)
8. Add your secret keys (from step 2) by making a new root-level file called tweepy.env and populating it as follows:
    consumer_key=''
    consumer_secret=''
    access_token=''
    access_token_secret=''
9. Do the same steps as above for new file spoonacular.env and add your hidden Spoonacular key from step 3 as:
    spoonacular_key=''.
10. Run `python Project1M1.py`
11. If on Cloud9, preview templates/index.html. This should successfully render the HTML!
12. Make sure to create a .gitignore by running touch .gitignore in your terminal and adding your .env files to it (so add tweepy.env and spoonacular.env)
13. A technical issue I ran into was getting my Github authentication to work. Because I have two-factor authentication enabled on my Github, it requires 
that a key be generated each time I log in, which wasn't happening via my terminal in C9. Thus it was not allowing me to login and push my code up to master. I 
resolved this by looking it up, and seeing that I had to generate a personal access token, and use that as the password when pushing my code which worked! If you
have a similar issue with 2 factor authentication you can do this too, the personal access token can be generated when you go to settings on Github.
14. Some issues that still exist in the app are that with caching, sometimes when you make changes to the CSS file, those changes are not shown. And so you have 
to clear the cache in your browsers settings each time. Another issue is that the auth_api.search() sometimes has no results and so you have to be careful of that. 
I would fix this by picking foods that return results and by hard refreshing my page.
