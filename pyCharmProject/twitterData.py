import array, numpy as np
from tweetTextManipulation import get_normalized_tweets
def create_tweets_data(files):
    #holds tweets
    x_data = []
    #holds information which tweet is from what file(topic)
    y_data = []

    for idx, file in enumerate(files):
        try:
            tweets = get_normalized_tweets(file)

        except RuntimeError, re:
            print "Error while extracting tweets from file", re
            continue
        x_data = np.concatenate((x_data, tweets))
        y_data = np.concatenate((y_data, [idx]*len(tweets)))
        print len(tweets)
    return x_data, y_data

def print_tweets_to_file(filename, tweets):
    file = open(filename, 'a')
    for tw in tweets:
        file.write(tw+'\n')

"""
X_train, y_train = create_tweets_data(["train_data/auto_tweets", "train_data/education_tweets", "train_data/fashion_tweets", "train_data/music_tweets", "train_data/science_tweets", "train_data/sport_tweets", "train_data/politics_tweets"])
X_test, y_test = create_tweets_data(["test_data/tw_auto_test", "test_data/tw_education_test", "test_data/tw_fashion_test","test_data/tw_music_test","test_data/tw_science_test", "test_data/tw_sport_test", "test_data/tw_politics_test"])

print_tweets_to_file('./all_tweets', X_train)
print_tweets_to_file('./all_tweets', X_test)
"""
#x_train, y_train =  create_tweets_data(["auto_tweets", "education_tweets", "fashion_tweets", "science_tweets", "sport_tweets", "games_tweets", "politics_tweets"])
#print "duzina: ", len(x_train),len(y_train)
#print x_train[0:10]

