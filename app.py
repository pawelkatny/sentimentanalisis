import InitialAnalysis as init
import TextProcessing as tp
import pandas as pd

file = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/tweets.csv'

def load_file(file_name):
    csv_data = pd.read_csv(file, names=['Date', 'Tweet', 'Language', 'Retweets', 'Likes'])

    return csv_data

def initial_analysis(data):
    #creating new object of InitialAnalysis class
    analysis = init.RawAnalysis(data)

    #counting all hashes in file
    hash = analysis.occurence_counter('hash')

    #apply function to 'Tweet' column to count length of every tweet
    tweets_len = analysis.tweets_len()

    #returns only data frame with quantity of retweets, likes and tweet length
    numeric_data = analysis.numeric_data_frame(tweets_len)

    return hash, numeric_data

def testing(some_data):
    print()


def app_init():

    data = load_file(file)

    hash, numeric_data = initial_analysis(data)

    print(hash)
    print(numeric_data)


app_init()