# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:20:38 2015

@author: Gavrilo
"""
#%%
import tweepy

print 8888
consumer_key = "F7oBOBomZ8PV4IAihzTxDukTG"
consumer_secret ="AHIGEIVXsjRUjJLCLcIbPNrcUHNjxXCZPcQWk68HPin2rnKTWo"
access_token = "250345600-RZkPghYzQgWwgCAn8MplKh1kXTay6GXC7IX9GubE"
access_token_secret = "KsRIJKVQt3JzxEJmpatkpZ2NnUqhsh2zsoZkyw66d02ei" 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_tweets = api.user_timeline('predsednikrs', None, None,None, None, 180, None)
print "Tvitovi korisnika", len(user_tweets)
public_tweets = api.home_timeline(None, None, 50, None)
#print len(public_tweets)
print user_tweets[1]
#for tweet in user_tweets:
#    print "*********************************\n",tweet.text,"\n***********************"
    
#%%