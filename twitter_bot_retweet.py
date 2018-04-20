import datetime
import os
import tweepy
from time import sleep
from creds import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

target_log_file = open('/var/log/twitter_bot/retweet_bot.log', 'a')


search_items = ['#100DaysOfCode', '#OpenStack', '#kubernetes', '#docker', '#netapp', '#netappateam', '#netappinsight', '#AWS', '#AWSSummit']

tweeted = False

def logging(search_item, username, if_failed, reason):

    if if_failed == True:

        #target_log_file.write('##########\n')
        #target_log_file.write('Tweet by @' + username + '\n')
        #target_log_file.write(reason + '\n')
        #target_log_file.write('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()) + '\n')
        #target_log_file.write('##########\n')

        print('##########')
        print('Tweet by @' + username)
        print(reason)
        print('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
        print('##########\n')

    else:

        #target_log_file.write('##########\n')
        #target_log_file.write('Tweet by @' + username + '\n')

        #target_log_file.write('Retweeted the tweet\n')
        #target_log_file.write('Search term was {}'.format(search_item) + '\n')
        #target_log_file.write('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()) + '\n')
        #target_log_file.write('##########\n')


        print('##########')
        print('Tweet by @' + username)
        print('Retweeted the tweet')
        print('Search term was {}'.format(search_item))
        print('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
        print('##########\n')


def retweet():

    for search in search_items:

        tweeted = False

        for tweet in tweepy.Cursor(api.search, q=search, lang='en').items(10):

            try:

                if tweeted == False:

                    tweet.retweet()

                    logging(search, tweet.user.screen_name, False, None)

                    tweeted = True

                else:

                    break

            except tweepy.TweepError as e:

                logging(search, tweet.user.screen_name, True, e.reason)

            except StopIteration:

                #target_log_file.write("An error occurred, restarting the script.\n")
                #target_log_file.write('##########\n')
                #target_log_file.write('##########\n')
                #target_log_file.write('##########\n')
                #target_log_file.close()

                sleep(120)
                os.system("python3 restart.py")
                break


        sleep(60)

    sleep(1200)




while True:
    retweet()
