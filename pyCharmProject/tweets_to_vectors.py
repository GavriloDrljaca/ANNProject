import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities, utils
from twitterData import *
from pprint import pprint  # pretty-printer


def create_dictionary(tweets_file, dictionary_name, stoplist):
    all_tweets_file = open(tweets_file, 'r')
    all_tweets = all_tweets_file.read()
    tw = all_tweets.replace("\\n", " ")
    stop_words = load_stoplist(stoplist)
    texts = [word for word in tw.lower().split() if word not in stop_words]

    dictionary = corpora.Dictionary([texts])
    dictionary.save(dictionary_name + '.dict')


def tweet_to_int_array(dict, tweet):
    ret_val = []
    new_vec = dict.doc2bow(tweet.lower().split())
    for idx, value in enumerate(new_vec):
        ret_val.append(value[0])
    return ret_val


def transfrom_tweets_to_arrays(dict, tweets):
    ret_val = []
    for tweet in tweets:
        ret_val.append(tweet_to_int_array(dict, tweet))
    return ret_val

def load_stoplist(file):
    stoplist_file = open(file, 'r')
    stoplist_words = stoplist_file.read()
    stoplist_words = stoplist_words.replace("\\n", " ")
    return stoplist_words.split();

"""
X_train, y_train = create_tweets_data(["train_data/auto_tweets",  "train_data/fashion_tweets", "train_data/music_tweets", "train_data/science_tweets", "train_data/sport_tweets", "train_data/politics_tweets"])
X_test, y_test = create_tweets_data(["test_data/tw_auto_test",  "test_data/tw_fashion_test","test_data/tw_music_test","test_data/tw_science_test", "test_data/tw_sport_test", "test_data/tw_politics_test"])

print_tweets_to_file('./all_tweets', X_train)
print_tweets_to_file('./all_tweets', X_test)

create_dictionary('all_tweets', 'test_dict', 'stoplist.txt')
dictionary = corpora.Dictionary
my_dict = dictionary.load('test_dict.dict')
print(my_dict)
"""