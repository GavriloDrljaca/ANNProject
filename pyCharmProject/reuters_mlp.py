'''Train and evaluate a simple MLP on the Reuters newswire topic classification task.
GPU run command:
    THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python examples/reuters_mlp.py
CPU run command:
    python examples/reuters_mlp.py
'''

from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.datasets import reuters
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from keras.preprocessing.text import Tokenizer
from tweets_to_vectors import *
from twitterData import *

max_words = 40000
batch_size = 32
nb_epoch = 5

print('Loading data...')
#(X_train, y_train), (X_test, y_test) = reuters.load_data(nb_words=None, test_split=0.2)

X_train, y_train = create_tweets_data(["train_data/auto_tweets", "train_data/education_tweets", "train_data/fashion_tweets", "train_data/music_tweets", "train_data/science_tweets", "train_data/sport_tweets", "train_data/politics_tweets"])

X_test, y_test = create_tweets_data(["test_data/tw_auto_test", "test_data/tw_education_test", "test_data/tw_fashion_test","test_data/tw_music_test","test_data/tw_science_test", "test_data/tw_sport_test", "test_data/tw_politics_test"])
#Loading dictionary
dictionary = corpora.Dictionary
my_dict = dictionary.load('test_dict.dict')
X_train = transfrom_tweets_to_arrays(my_dict, X_train)
#X_train = np.array(X_train)
#y_train = np.array(y_train)
X_test = transfrom_tweets_to_arrays(my_dict, X_test)
X_test = np.array(X_test)
y_test = np.array(y_test)
alphabet = ["auto", "education", "fashion", "music", "science", "sport", "politics"]
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

nb_classes = np.max(y_train)+1
print(nb_classes, 'classes')

print('Vectorizing sequence data...')
tokenizer = Tokenizer(nb_words=max_words)
X_train = tokenizer.sequences_to_matrix(X_train, mode='binary')
X_test = tokenizer.sequences_to_matrix(X_test, mode='binary')
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Convert class vector to binary class matrix (for use with categorical_crossentropy)')
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)
print('Y_train shape:', Y_train.shape)
print('Y_test shape:', Y_test.shape)

print('Building model...')
model = Sequential()
model.add(Dense(512, input_shape=(max_words,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

history = model.fit(X_train, Y_train, nb_epoch=nb_epoch, batch_size=batch_size, verbose=1, show_accuracy=True, validation_split=0.1)
score = model.evaluate(X_test, Y_test, batch_size=batch_size, verbose=1, show_accuracy=True)
print('Test score:', score[0])
print('Test accuracy:', score[1])