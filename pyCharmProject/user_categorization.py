from keras.models import model_from_json
from gensim import corpora
from tweepy import TweepError
from twitterData import *
from retriveTweets import get_tweets_from_user
from tweets_to_vectors import *
from keras.preprocessing import sequence
from resultAnalysis import *

maxlen = 20
batch_size = 32

"""
Loading saved CNN and dictionary
"""
print "Loading saved CNN (CNN_6ep_230edims) and dictionary \n"
model = model_from_json(open('saved_models/CNN_noED_6ep2.json').read())
model.load_weights('saved_models/CNN_noED_6ep_weights2.h5')

dictionary = corpora.Dictionary
my_dict = dictionary.load('test_dict.dict')

"""
Retriving tweets from some twitter user based on input userID
"""
print "Retriving tweets from some twitter user based on input userID \n"

userID = raw_input("Enter twiter user id: ")
#num_of_tweets_to_retrive = raw_input("Enter number of tweets to retrive: ")
user_tweets = []
try:
    user_tweets= get_tweets_from_user(userID,  200)
except TweepError, e:
    print "Error retrieving user id's", e

"""
Preprocesing tweets so they can be used as input for artificial neural network (in our case CNN)
"""
print "Preprocesing tweets so they can be used as input for artificial neural network (in our case CNN)\n"
user_tweets_filename = 'user_tweets/'+userID+'.txt'
print_tweets_to_file(user_tweets_filename, user_tweets)
X_data, y_data = create_tweets_data([user_tweets_filename])
X_data = transfrom_tweets_to_arrays(my_dict, X_data)
X_data = sequence.pad_sequences(X_data, maxlen=maxlen, padding='post')
"""
Categorization of input data
"""
print "Categorization of input data. Length of input: ", X_data.shape, "\n"
result = model.predict(X_data, 32)
results = winner_array(result, cut=False)
topic_percent =  calculate_topic_percent(results)
alphabet = ["auto", "fashion", "music", "science", "sport", "politics", "other"]

print "\n RESULTS: \n"
print print_results_by_topic(alphabet, topic_percent)