import tweepy
from creds import *
from time import sleep


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file = open('random.txt', 'r')
file_lines = my_file.readlines()
my_file.close()


def tweet():

    for line in file_lines:

        try:
            print(line)
            if line != '\n':
                # api.update_status(line)
                # rate_limit = api.rate_limit_status()
                # print(rate_limit)

                mentions = api.mentions_timeline
                print(mentions)
                sleep(900)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

    my_file.close


tweet()


