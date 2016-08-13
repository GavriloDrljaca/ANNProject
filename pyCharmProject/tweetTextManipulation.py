import json, numpy as np

def extract_tweets_from_file(filename):
    with open(filename, 'r') as text_file:
        tweets_sport = []
        for line in text_file:
            line = line[1:-1]
            new_line = line.replace('"', "'")
            tweets = []
            tweets = new_line.split("', '")
            tweets_sport = np.concatenate((tweets_sport, tweets))
    return tweets_sport

def normalize_tweets(tweets):
    """
    Normalization consists of removing links from status, codes that are not ascii like \x80 etc
    and removing new line, also removing tweets shorter then 10chars
    :param tweets: array of textual tweets
    :return: array of normalized textual tweets
    """
    normalized_tweets = []
    for tw in tweets:
        tw = remove_http_from_tweet(tw)
        tw = tw.replace("\\xe2\\x80\\x99", "'")
        tw = remove_bad_codes_from_tweet(tw)
        tw = tw.replace("\\n", " ")
        #Uklanjanje neiformativnih znakova
        tw = tw.replace("@", "AT ")
        tw = tw.replace("#", " ")
        tw = tw.replace(",", " ")
        tw = tw.replace(".", " ")
        tw = tw.replace("\|", " ")
        tw = tw.replace("\[", " ")
        tw = tw.replace("\]", " ")
        tw = tw.replace("!", " ")
        tw = tw.replace("/", " ")
        tw = tw.replace("_", " ")

        if(len(tw)>20):
            normalized_tweets.append(tw)
            if tw[0] == "'":
                tw = tw[1:]
    return normalized_tweets


def remove_http_from_tweet(tweet):
    http_position = tweet.find("http")

    while (http_position != -1):
        curr_pos = http_position
        while (tweet[curr_pos] != " " and curr_pos < len(tweet) - 1):
            tweet = tweet[:curr_pos] + tweet[curr_pos + 1:]
        tweet = tweet[:curr_pos] + tweet[curr_pos + 1:]
        http_position = tweet.find("http")
    return tweet


def remove_bad_codes_from_tweet(tweet):
    code_position = tweet.find("\\x")
    while (code_position != -1):
        curr_pos = code_position
        deleted = 0
        while (tweet[curr_pos] != " " and curr_pos < len(tweet) - 1 and deleted < 4):
            tweet = tweet[:curr_pos] + tweet[curr_pos + 1:]
            deleted += 1
        # tweet = tweet[:curr_pos] + tweet[curr_pos+1:]
        code_position = tweet.find("\\x")
    return tweet

def get_normalized_tweets(filename):
    tweets = extract_tweets_from_file(filename)
    return normalize_tweets(tweets)
