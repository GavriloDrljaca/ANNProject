"""
Created on Sun Jan 3 2016
@autohor Gavrilo Drljaca
"""

import tweepy, json
from getTrainTweets import get_train_tweets
def get_tweets(tag, number_of_tweets, date):
    consumer_key = "F7oBOBomZ8PV4IAihzTxDukTG"
    consumer_secret ="AHIGEIVXsjRUjJLCLcIbPNrcUHNjxXCZPcQWk68HPin2rnKTWo"
    access_token = "250345600-RZkPghYzQgWwgCAn8MplKh1kXTay6GXC7IX9GubE"
    access_token_secret = "KsRIJKVQt3JzxEJmpatkpZ2NnUqhsh2zsoZkyw66d02ei"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweetsID = get_train_tweets(tag, number_of_tweets, date)
    print len(tweetsID)
    tweets_text = []
    for id in tweetsID:
        try:
            status = api.get_status(id)
            tweets_text.append(status)
        except tweepy.error.TweepError, e:
            print e
    return tweets_text

tweets = get_tweets('fashion', '180', '2015-12-20')
file_sport = open('fashion_tweets', 'a')
tweet_statuses = []
for tweet in tweets:
   tweet_statuses.append(tweet.text.encode('utf-8'))
file_sport.write(tweet_statuses.__str__())
file_sport.write("\n")
