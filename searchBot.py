import tweepy
import time
import os

# get api keys from .env file
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
key = os.environ.get('KEY')
secret = os.environ.get('SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

wait_time = 60
hashtag = "#cosplay"
tweetNumber = 10
# get last 10 hashtag items
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

# retweets tweets with #cosplay tag


def searchBot():
    for tweet in tweets:
        try:
            tweet.favorite()
            tweet.retweet()
            print("Retweet done!")
            time.sleep(wait_time)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(wait_time)
