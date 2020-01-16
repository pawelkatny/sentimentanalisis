import InitialAnalysis as init
import TextProcessing as tp
import pandas as pd

file = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/tweets.csv'

def load_file(file_name):
    csv_data = pd.read_csv(file, names=['Date', 'Tweet', 'Language', 'Retweets', 'Likes'])

    return csv_data

def initial_analysis(data):
    #creating new object of InitialAnalysis class
    analysis = init.InitialAnalysis(data)

    #counting all hashes in file
    hash_tags = analysis.occurence_counter('hash')

    #apply function to 'Tweet' column to count length of every tweet
    tweets_len = analysis.tweets_len()

    #returns data frame with added tweet length
    new_data = analysis.append_data_frame(tweets_len, tweets_len.name)

    return hash_tags, new_data


def process_text(data):

    text_process = tp.TextProcessing(data['Tweet'])
    clean_tweets = text_process.clean_all_tweets()

    return  clean_tweets

def testing(some_data):
    print(some_data)


def app_init():

    data = load_file(file)

    hash, new_data = initial_analysis(data)

    clean_tweets = process_text(data)

    print(hash)
    print(new_data)
    print(clean_tweets)

app_init()