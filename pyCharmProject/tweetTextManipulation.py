
import json, numpy as np
def extract_tweets_from_file(filename):
    with open(filename,'r') as text_file:
        tweets_sport = []
        for line in text_file:
            line =  line[1:-1]
            new_line = line.replace('"', "'")
            tweets = []
            tweets = new_line.split("', '")
            tweets_sport  = np.concatenate((tweets_sport, tweets))
    return tweets_sport

def normalize_tweets(tweets):
    normalized_tweets = []
    for tw in tweets:
        tw = remove_http_from_tweet(tw)
        tw = remove_bad_codes_from_tweet(tw)
        tw = tw.replace("\\n", " ")
        normalized_tweets.append(tw)

    return normalized_tweets

def remove_http_from_tweet(tweet):
    http_position = tweet.find("http")

    while(http_position != -1):
        curr_pos = http_position
        while(tweet[curr_pos] != " " and curr_pos<len(tweet)-1):
            tweet = tweet[:curr_pos] + tweet[curr_pos+1:]
        tweet = tweet[:curr_pos] + tweet[curr_pos+1:]
        http_position = tweet.find("http")
    return tweet
def remove_bad_codes_from_tweet(tweet):
    code_position = tweet.find("\\x")
    while(code_position != -1):
        curr_pos = code_position
        deleted = 0
        while(tweet[curr_pos] != " " and curr_pos<len(tweet)-1 and deleted<4):
            tweet = tweet[:curr_pos] + tweet[curr_pos+1:]
            deleted+=1
        #tweet = tweet[:curr_pos] + tweet[curr_pos+1:]
        code_position = tweet.find("\\x")
    return tweet
tweets = extract_tweets_from_file("sport_tweets")
tweets = normalize_tweets(tweets[0:100])
print tweets[0:50]


