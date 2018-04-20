To get this twitter bot to work correctly, you will need to do the following:

 1. Make sure your running python. I used Python3 for my twitter bot
 2. Install Tweepy, this is the python framework I used for my twitter API calls.
 3. Create a new file called creds.py.

    In that file include the following:

    consumer_key = 'Your Twitter Consumer Key'
    
    consumer_secret = 'Your Twitter Consumer Secret'
    
    access_token = 'Your Twitter Access Token'
    
    access_token_secret = 'Your Twitter Access Token Secret'
    

If you need more information on this file and the steps I used to create this bot then check out:

https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library#keeping-the-twitterbot-running


I've just been using the twitter_bot_retweet.py script, others are still a work in progress.

I run the bot with the following command:

nohup python3 -u twitter_bot_retweet.py &

This removes it from my console session and allows it to run. All the print statements in the logging funciton will then get put into the
nohup.out file.
