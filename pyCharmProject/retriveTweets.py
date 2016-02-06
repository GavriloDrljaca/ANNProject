"""
Created on Sun Jan 3 2016
@autohor Gavrilo Drljaca
"""

import tweepy, json
from urllib2 import Request, urlopen, URLError


# tag can be sport, politics and etc, date is in YYYY-MM-DD format
def get_train_tweets(tag, number_of_pages, date):
    num_plus = int(number_of_pages)
    request_string = 'http://influencedb.com/buzz-api/api/twitter/tweets?skip=0&take=' + str(num_plus) + '&tags=' + tag + '&cacheOnly=false&showResultsFromSolr=false&isoDate=' + date + '&language=en&_=1451483470386'
    request = Request(request_string)
    try:
        response = urlopen(request)
        tweets = response.read()
    except URLError, e:
        print "Error retrieving tweets from influence.db ", e

    json_tweets = json.loads(tweets);

    tweetsID = []
    for tw in json_tweets['data']:
        id_string = tw['statusId']
        # id_string = id_string.lstrip()
        tweetsID.append(int(id_string))
    return tweetsID


def create_OAuth():
    consumer_key = "F7oBOBomZ8PV4IAihzTxDukTG"
    consumer_secret = "AHIGEIVXsjRUjJLCLcIbPNrcUHNjxXCZPcQWk68HPin2rnKTWo"
    access_token = "250345600-RZkPghYzQgWwgCAn8MplKh1kXTay6GXC7IX9GubE"
    access_token_secret = "KsRIJKVQt3JzxEJmpatkpZ2NnUqhsh2zsoZkyw66d02ei"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth

def get_tweets_from_user(userID):
    api =tweepy.API(create_OAuth())

    tweets = api.user_timeline(userID, None, None, 200,None)

    ret =[]
    for tw in tweets:
        ret.append(tw.text)

    return ret


def get_tweets(tag, number_of_tweets, date):
    api = tweepy.API(create_OAuth())

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


tweets = get_tweets('sport', '180', '2016-01-03')
file_sport = open('train_data/sport_tweets', 'a')
tweet_statuses = []
for tweet in tweets:
    tweet_statuses.append(tweet.text.encode('utf-8'))
file_sport.write(tweet_statuses.__str__())
file_sport.write("\n")