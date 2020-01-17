from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import csv
import simplejson as json

ACCESS_TOKEN = "425801861-ePnK1pLEu0mNB2nL2y92b7Xrv6ySwRVc4WfGlCi0"
ACCESS_TOKEN_SECRET = "06ZrqDfTyYhlU4otb8933Kree7Um9rS4yIq3FIAuw4nLn"
CONSUMER_KEY = "67DBM6o7mxCnwUsaeD1J2ieAR"
CONSUMER_SECRET = "woi1vNtpgHr20bA8NOiVbNL4O4cB3QpqVZHhKGNb2Qm0BidhqB"
 
class TwitterStreamer():
   
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        
        stream.filter(track=hash_tag_list)


class StdOutListener(StreamListener):
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            
            w = json.loads(data)
            date = w['created_at']
            text = w['text']
            retweet = w['retweeted_status']['retweet_count']
            favorite = w['retweeted_status']['favorite_count']
            lang= w['lang']
            formattext = text.split(':')[1]          
                                        
            with open('tweets.csv', 'a',newline='') as tf:
              writter = csv.writer(tf)
              writter.writerow([date,formattext,lang,retweet,favorite])                 
                  
                             
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print('hello')
        print(status)

if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ['Donald Trump']
    fetched_tweets_filename = "tweets.csv"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
