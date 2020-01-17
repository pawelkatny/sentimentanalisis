import InitialAnalysis as init
import TextProcessing as tp
import Prediction as pre
from Functions import *
import Sentiment as st

file = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/tweety.csv'
path = '/mnt/02546E3B546E3199/Study/Python/sentimentanalysis/data/'

def load_file(file_name):
    csv_data = pd.read_csv(file, names=['Date', 'Tweet', 'Language', 'Retweets', 'Likes'], encoding='utf-8')

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

def show_results(args):
    print(f'{args[0]}:\n {args[1]}')

def app_init():

    data = load_file(file)

    #get data frame with hash list and data frame with appended tweet length and hash count column
    hash, initial_data = initial_analysis(data)

    #clean tweets to use them for sentiment analysis, returns also tfid text vectors
    clean_tweets, deep_clean_tweets, vectors = process_text(data)

    #adds clean and lemmatised sentences to initial_data frame
    initial_data = append_to_data_frame(initial_data, 'Lemmatized_text', deep_clean_tweets)
    #run sentiment analysis and return new data frame with appended columns with sentiment analysis
    sentiment_data = analyse_sentiment(initial_data, clean_tweets)

    test = sentiment_data['Nltk_Sentiment']
    prediction = pre.Prediction(vectors, test)
    prediction_accuracy, sentiment_prediction = prediction.predict_sentiment()

    sentiment_data = append_to_data_frame(sentiment_data, 'Predicted_sentiment', sentiment_prediction)

    save_file('new_data_frame.csv', sentiment_data)

    print_sent = ['Sentiment analysis results', sentiment_data.iloc[:, 5:]]
    print_acc = ['Prediction accuracy for machine learning model', prediction_accuracy]

    show_results(print_sent)
    show_results(print_acc)


app_init()