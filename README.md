
# RecipeApp
This is a Web Application that displays a Tweet using Tweepy and a relevant image from Spoonacular using the Spoonacular API from a users ingredient input.

Language/Technologies Used: **Python, Flask, Tweepy, Spoonacular API, Heroku**
## View this app at: https://desolate-wildwood-92632.herokuapp.com/

To use this repository, you must follow these steps:
## Initial Setup
0. Sign up for the twitter developer portal at https://developer.twitter.com
1. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
2. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
    > If needed, you can regenerate your access token and secret.
3. Sign up for the spoonacular account at https://spoonacular.com/food-api. Navigate to my console, then profile and copy your hidden keys.
4. Clone this repository by using git clone https://github.com/AaratiS12/SeniorCapstone-Project1.git
## Steps to Run
6. Run the following in your terminal:
    `sudo pip install tweepy`
    (or) `sudo pip3 install tweepy`
    (or) `pip install tweepy`
    (or) `pip3 install tweepy`
7. Install flask using the same process as above: `[sudo] pip[3] install flask`
8. Install requests using the same process as above: `[sudo] pip[3] install requests`
9. Add your secret keys (from step 2) by making a new root-level file called tweepy.env and populating it as follows:
    `consumer_key=''`
    `consumer_secret=''`
    `access_token=''`
    `access_token_secret=''`
10. Do the same steps as above for new file spoonacular.env and add your hidden Spoonacular key from step 3 as:  `spoonacular_key=''`
11. If you would like to input a food run: `python userInput.py` else run: `'python noUserInput.py'`
12. If on Cloud9, preview templates/index.html. This should successfully render the HTML!
13. Make sure to create a .gitignore by running `touch .gitignore` in your terminal and adding your .env files to it (so add tweepy.env and spoonacular.env)
14. The next step is to sign up for heroku at heroku.com and Install heroku by running `npm install -g heroku`
## Heroku Setup
16. Then run
    `heroku login -i`
    `heroku create`
    `git push heroku master` and make sure your origin is correct by running `git remote -v`
17. Add your secret keys (from tweepy.env and spponacular.env) by going to https://dashboard.heroku.com/apps
    and clicking into your app. Click on Settings, then scroll to "Config Vars." Click
    "Reveal Config Vars" and add the key value pairs for each variable and make sure they are names exactly the same as the variables in your python script.
18. Configure requirements.txt with all requirements needed to run your app by runnning 'pip freeze > requirements.txt'
19. Configure Procfile with the command needed to run your app 

# Technical Issues
18. A technical issue I ran into was getting my Github authentication to work. Because I have two-factor authentication enabled on my Github, it requires 
that a key be generated each time I log in, which wasn't happening via my terminal in C9. Thus it was not allowing me to login and push my code up to master. I resolved this when I found https://medium.com/@ginnyfahs/github-error-authentication-failed-from-command-line-3a545bfd0ca8 and I had to generate a personal access token, and use that as the password when pushing my code which worked! If you have a similar issue with 2 factor authentication you can do this too, the personal access token can be generated when you go to settings > Developer Access on Github. A token can be regenerated but you lose it once you close out of the box.
19. Another issue I had while deploying to Heroku was that I was getting an error when running push heroku master. I had not created a requirements.txt file or Procfile but once they were created I was able to push the code to Heroku.
21. Sometimes the twitter search API returns with no items, and so I ran into issues where the web page would not load. I added code to catch that and display "No Tweet" on the page instead.
22. Some issues that still exist in the app are that with caching, sometimes when you make changes to the CSS file, those changes are not shown. And so you have to clear the cache in your browsers settings each time by hard refreshing my page(ctrl + shift + r)
23. An additional feature I would add is consolidating my 2 python files (one for user input one without user input) into one file, that can be run using a flag option. So for example I would add requirements such that if it is run with 'python Project1M1.py --no_input' that it would not take a user input and would randomly select one of the 7 item in the items list. I would use --no_input as a boolean for my script, and that if it is present I use the list values.
