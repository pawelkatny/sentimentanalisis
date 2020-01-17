import InitialAnalysis as init
import TextProcessing as tp
import pandas as pd
from Functions import *
import Sentiment as st

file = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/tweets_final.csv'
path = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/'

def load_file(file_name):
    csv_data = pd.read_csv(file, names=['Date', 'Tweet', 'Language', 'Retweets', 'Likes'], encoding='utf-8')

    print(csv_data)
    return csv_data

def save_file(file_name, data_frame):
    data_frame.to_csv(path + file_name, index=False)


def initial_analysis(data):
    #creating new object of InitialAnalysis class
    analysis = init.InitialAnalysis(data)

    #counting all hashes in file
    hash_tags, hash__tags_counter = analysis.occurence_counter('hash')

    #apply function to 'Tweet' column to count length of every tweet
    tweets_len = analysis.tweets_len()

    #returns data frame with added tweet length and hashtags count
    new_data = append_to_data_frame(data, tweets_len.name, tweets_len)
    new_data = append_to_data_frame(new_data, 'Hashtags', hash__tags_counter)

    return hash_tags, new_data


def process_text(data):

    text_process = tp.TextProcessing(data['Tweet'])
    clean_tweets = text_process.clean_all_tweets()

    deep_clean_tweets = text_process.deep_clean_all_tweets()

    vectors = text_process.vectorise()

    return  clean_tweets, deep_clean_tweets, vectors

def analyse_sentiment(data, tweets):

    analyser = st.Sentiment(tweets)
    vader_sentiments, vader_score  = analyser.check_sentiment_vader()
    vader_data = append_to_data_frame(data, 'Nltk_Sentiment_Score', vader_score)
    vader_data = append_to_data_frame(vader_data, 'Nltk_Sentiment', vader_sentiments)

    return vader_data

def show_results(some_data):
    print(some_data)


def app_init():

    data = load_file(file)

    #get data frame with hash list and data frame with appended tweet length and hash count column
    hash, initial_data = initial_analysis(data)

    #clean tweets to use them for sentiment analysis, returns also tfid text vectors
    clean_tweets, deep_clean_tweets, vectors = process_text(data)

    #adds clean and lemmatised sentences to initial_data frame
    initial_data = append_to_data_frame(initial_data, 'Lemmatised_text', deep_clean_tweets)
    #run sentiment analysis and return new data frame with appended columns with sentiment analysis
    sentiment_data = analyse_sentiment(initial_data, clean_tweets)


    # print(vectors)
    # print(hash)
    # print(new_data)
    # print(clean_tweets)
    # print(deep_clean_tweets)
    print(sentiment_data)
    # print(sentiment_data.describe().astype(float))
    print(sentiment_data.describe().applymap("{:.2f}".format))
    print(sentiment_data['Nltk_Sentiment'].describe())
    save_file('new_data_frame.csv', sentiment_data)

app_init()