import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities, utils
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
create_dictionary('all_tweets', 'test_dict', 'stoplist.txt')
dictionary = corpora.Dictionary
my_dict = dictionary.load('test_dict.dict')
print(my_dict)
"""
"""
new_doc = ["He brought joy to millions @TomCruise surprises",
           "@JeffGordonWeb at  #NASCARawards with a special send off! #AskMRN",
           "ADIDAS IS NOT PLAYIN THIS YEAR"]
# new_vec = my_dict.doc2bow(new_doc.lower().split())
result = transfrom_tweets_to_arrays(my_dict, new_doc)
pprint(result)
print len(result)
"""
