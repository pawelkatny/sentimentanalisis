import pandas as pd
import nltk

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from Functions import *
import Loader as ld


class Sentiment():

    def __init__(self, tweets):
        self.tweets = tweets
        self.size = len(self.tweets)


    def check_sentiment_vader(self):
        loader = ld.Loader(self.size)

        sent_analyzer = SentimentIntensityAnalyzer()

        def apply_score(tweet):
            loader.loading()
            return sent_analyzer.polarity_scores(tweet)

        def sentiment_value(compound):
            value =''
            if compound < -0.05: value = 'negative'
            elif compound > 0.05: value = 'positive'
            else: value = 'neutral'

            return value


        f = lambda x: apply_score(x)
        g = lambda x: sentiment_value(x)


        sentiment_scores = self.tweets.apply(f) #returns data frame of dictionaries
        sentiment_scores = sentiment_scores.apply(pd.Series) #splits dictionaries with keys as columns
        sentiment_compound = sentiment_scores['compound']
        sentiment_values = sentiment_compound.apply(g)

        return sentiment_values, sentiment_compound
