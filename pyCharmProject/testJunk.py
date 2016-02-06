from retriveTweets import get_tweets_from_user
from tweetTextManipulation import normalize_tweets
tweets = get_tweets_from_user("nytimes")


print normalize_tweets(tweets)[0]