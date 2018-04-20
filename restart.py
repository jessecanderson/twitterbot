import os
from time import sleep


def restart():
    sleep(900)

    os.system("nohup python3 -u twitter_bot_retweet.py &")



restart()