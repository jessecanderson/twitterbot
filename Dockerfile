FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /var/log/twitter_bot/
RUN touch /var/log/twitter_bot/retweet_bot.log

COPY . ./

CMD [ "python", "./twitter_bot_retweet.py" ]
