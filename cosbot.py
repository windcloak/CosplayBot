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

FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#cosplaybotchan' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name +
                            " Nice! :)", tweet.id)
            api.create_favorite(tweet.id)
            
            store_last_seen(FILE_NAME, tweet.id)

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


while True:
    reply()
    time.sleep(wait_time)
    searchBot()
