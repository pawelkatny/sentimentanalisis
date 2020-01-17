import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('stopwords')
from Patterns import patterns_list as patterns

class TextProcessing():

    def __init__(self, tweets):
        self.tweets = tweets
        self.clean_tweets = None
        self.deep_clean_tweets = None
        self.vectors = None
        self.lemmatizer = WordNetLemmatizer()


    def clean(self, tweet):
        clean_tweet = re.sub(patterns['http'], '', tweet)
        clean_tweet = re.sub(patterns['at'], '', clean_tweet)
        clean_tweet = re.sub(patterns['hash'], '', clean_tweet)
        clean_tweet = re.sub(patterns['amp'], 'and', clean_tweet)
        clean_tweet = re.sub(patterns['numbers'], ' ', clean_tweet)

        return clean_tweet

    def deep_clean(self, clean_text):
        stops = set(stopwords.words('english'))

        deep_clean_tweet = re.sub(patterns['special_chars'], ' ', clean_text)
        deep_clean_tweet = re.sub(patterns['single_char'], ' ', deep_clean_tweet)
        deep_clean_tweet = deep_clean_tweet.lower()
        deep_clean_tweet = deep_clean_tweet.split()
        deep_clean_tweet = [word for word in deep_clean_tweet if not word in stops]
        deep_clean_tweet = [self.lemmatizer.lemmatize(word) for word in deep_clean_tweet]
        deep_clean_tweet = ' '.join(deep_clean_tweet)

        return  deep_clean_tweet


    def clean_all_tweets(self):
        f = lambda x: self.clean(x)
        clean_tweets = self.tweets.apply(f)
        self.clean_tweets = clean_tweets

        return clean_tweets


    def deep_clean_all_tweets(self):
        f = lambda x: self.deep_clean(x)
        deep_clean_tweets = self.clean_tweets.apply(f)
        self.deep_clean_tweets = deep_clean_tweets

        return deep_clean_tweets

    def vectorise(self):
        tfid_converter = TfidfVectorizer(max_features=1000, min_df=1, max_df=0.7)
        vectors_text = tfid_converter.fit_transform(self.deep_clean_tweets)
        self.vectors = vectors_text

        return vectors_text