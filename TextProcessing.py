import re
from patterns import patterns_list as patterns

class TextProcessing():

    def __init__(self, tweets):
        self.tweets = tweets

    def clean_tweet(self, tweet):
        clean_tweet = re.sub(patterns['http'], '', tweet)
        clean_tweet = re.sub(patterns['at'], '', clean_tweet)
        clean_tweet = re.sub(patterns['hash'], '', clean_tweet)
        clean_tweet = re.sub(patterns['amp'], 'and', clean_tweet)

        return clean_tweet

    def clean_all_tweets(self):
        f = lambda x: self.clean_tweet(x)
        clean_tweets = self.tweets.apply(f)

        return clean_tweets

