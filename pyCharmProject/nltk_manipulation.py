import nltk
import string
from tweetTextManipulation import *
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.regexp import RegexpStemmer

#nltk.download()


def stem_tweet(tweet, stemmer_type = "lancaster"):
    """
    :param tweet: string representing tweet
    :param stemmer_type: type of stemmer used (default value is lancaster)
    :type tweet: str
    :type stemmer_type: str
    """
    tokens = nltk.word_tokenize(tweet)
    stemmed_tokens = []
    if stemmer_type == "lancaster":
        stemmer = LancasterStemmer()
    elif stemmer_type == "snowball":
        stemmer = SnowballStemmer("english")
    elif stemmer_type == "porter":
        stemmer = PorterStemmer()
    elif stemmer_type == "regexp":
        stemmer = RegexpStemmer("english")
    else:
        return None

    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))

    ret_tw = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in stemmed_tokens]).strip()
    return ret_tw


tweets = extract_tweets_from_file("train_data/sport_tweets")
tweets = tweets[200:220]

for tweet in tweets:
    print("Original: " + tweet)
    print("Lancaster: " + stem_tweet(tweet, "lancaster"))
    print("Snowball: " + stem_tweet(tweet, "snowball"))
    print("Porter: " + stem_tweet(tweet, "porter"))
    print("Regexp: " + stem_tweet(tweet, "regexp"))