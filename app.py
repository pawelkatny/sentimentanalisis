import InitialAnalysis as init
import TextProcessing as tp
import pandas as pd
from Functions import *
import Sentiment as st

file = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/tweets.csv'
path = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/'

def load_file(file_name):
    csv_data = pd.read_csv(file, names=['Date', 'Tweet', 'Language', 'Retweets', 'Likes'])

    return csv_data

def save_file(file_name, data_frame):
    data_frame.to_csv(path + file_name)


def initial_analysis(data):
    #creating new object of InitialAnalysis class
    analysis = init.InitialAnalysis(data)

    #counting all hashes in file
    hash_tags, hash__tags_counter = analysis.occurence_counter('hash')

    #apply function to 'Tweet' column to count length of every tweet
    tweets_len = analysis.tweets_len()

    #returns data frame with added tweet length
    new_data = append_to_data_frame(data, tweets_len.name, tweets_len)
    new_data = append_to_data_frame(new_data, 'Hashtags', hash__tags_counter)

    return hash_tags, new_data


def process_text(data):

    text_process = tp.TextProcessing(data['Tweet'])
    clean_tweets = text_process.clean_all_tweets()

    return  clean_tweets

def analyse_sentiment(data, tweets):

    analyser = st.Sentiment(tweets)
    print(analyser.tweets)
    vader_sentiments, vader_score  = analyser.check_sentiment_vader()
    print(vader_sentiments)
    vader_data = append_to_data_frame(data, 'Nltk Sentiment Score', vader_score)
    vader_data = append_to_data_frame(vader_data, 'Nltk Sentiment', vader_sentiments)

    return vader_data

def testing(some_data):
    print(some_data)


def app_init():

    data = load_file(file)

    hash, new_data = initial_analysis(data)

    clean_tweets = process_text(data)

    sentiment_vader = analyse_sentiment(new_data, clean_tweets)

    print(hash)
    print(new_data)
    print(clean_tweets)
    print(sentiment_vader)

    save_file('new_data_frame.csv', sentiment_vader)

app_init()