'''This example demonstrates the use of Convolution1D for text classification.
Run on GPU: THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python imdb_cnn.py
Get to 0.835 test accuracy after 2 epochs. 100s/epoch on K520 GPU.
'''

from __future__ import print_function
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.convolutional import Convolution1D, MaxPooling1D
from twitterData import *
from gensim import corpora
from tweets_to_vectors import *
from keras.utils import np_utils
from keras.optimizers import SGD
import numpy as np
np.random.seed(1337)  # for reproducibility


def create_CNN_MODEL(model_file_name, dictionary_file,stemmer_type='none'):
    """
    :param model_file_name: name of the saved cnn model and it's weights
    :param dictionary_file: name of the dictionary used(it should be in correlation with stemmer)
    :param stemmer_type:  type of stemmer used to stem tweets (lancaster, porter, snowball, regexp or none)
    """
    # set parameters:
    max_features = 40000
    maxlen = 20
    batch_size = 32
    embedding_dims = 220
    nb_filter = 250
    filter_length = 3
    hidden_dims = 250
    nb_epoch = 6
    nb_classes =6

    print('Loading data...')

    X_train, y_train = create_tweets_data(["train_data/auto_tweets",  "train_data/fashion_tweets", "train_data/music_tweets", "train_data/science_tweets", "train_data/sport_tweets", "train_data/politics_tweets"])
    X_test, y_test = create_tweets_data(["test_data/tw_auto_test", "test_data/tw_fashion_test","test_data/tw_music_test","test_data/tw_science_test", "test_data/tw_sport_test", "test_data/tw_politics_test"])
    if(stemmer_type != 'none'):
        X_train = stemm_train_of_tweets(X_train, stemmer_type)
        X_test = stemm_train_of_tweets(X_test, stemmer_type)

    #Loading dictionary
    dictionary = corpora.Dictionary
    my_dict = dictionary.load(dictionary_file)
    X_train = transfrom_tweets_to_arrays(my_dict, X_train)
    X_test = transfrom_tweets_to_arrays(my_dict, X_test)

    alphabet = ["auto", "fashion", "music", "science", "sport", "politics"]
    print(len(X_train), 'train sequences')
    print(len(X_test), 'test sequences')

    print('Pad sequences (samples x time)')
    X_train = sequence.pad_sequences(X_train, maxlen=maxlen, padding='post')
    X_test = sequence.pad_sequences(X_test, maxlen=maxlen, padding='post')
    print('X_train shape:', X_train.shape)
    print('X_test shape:', X_test.shape)

    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)

    print('Build model...')
    model = Sequential()

    # we start off with an efficient embedding layer which maps
    # our vocab indices into embedding_dims dimensions
    model.add(Embedding(max_features, embedding_dims, input_length=maxlen))
    model.add(Dropout(0.25))

    # we add a Convolution1D, which will learn nb_filter
    # word group filters of size filter_length:
    model.add(Convolution1D(nb_filter=nb_filter,
                            filter_length=filter_length,
                            border_mode='valid',
                            activation='relu',
                            subsample_length=1))
    # we use standard max pooling (halving the output of the previous layer):
    model.add(MaxPooling1D(pool_length=2))

    # We flatten the output of the conv layer,
    # so that we can add a vanilla dense layer:
    model.add(Flatten())

    # We add a vanilla hidden layer:
    model.add(Dense(hidden_dims))
    model.add(Activation('relu'))
    model.add(Dropout(0.25))

    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop', metrics =["accuracy"])
    model.fit(X_train, Y_train, batch_size=batch_size,
              nb_epoch=nb_epoch, validation_data=(X_test, Y_test))

    score, acc = model.evaluate(X_test, Y_test, batch_size=batch_size)
    print('Test score:', score)
    print('Test accuracy:', acc)

    json_string = model.to_json()
    open('saved_models/'+model_file_name+'.json', 'w').write(json_string)
    model.save_weights('saved_models/'+model_file_name+'.h5')


create_CNN_MODEL('lancaster_model', 'dictionaries/lancaster_dictionary.dict', 'lancaster')