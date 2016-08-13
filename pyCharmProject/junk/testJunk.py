from retriveTweets import get_tweets_from_user
from tweetTextManipulation import normalize_tweets

from twitterData import *
X_train, y_train = create_tweets_data(["train_data/auto_tweets", "train_data/education_tweets", "train_data/fashion_tweets", "train_data/music_tweets", "train_data/science_tweets", "train_data/sport_tweets", "train_data/politics_tweets"])

num_of = 0
for t in X_train:
    if len(t)<10:
        print t
        num_of +=1

print "OOV: ", num_of

