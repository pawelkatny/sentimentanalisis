import re
from Patterns import patterns_list as patterns #regex patterns list
import Loader as ld  # prints current progress
from Functions import *

class InitialAnalysis():

    def __init__(self, data):
        self.data = data
        self.tweets = data['Tweet']
        self.size = len(data)

    def occurence_counter(self, key):  # emots, hash etc counter - returns descending sorted array
                                        # and panda data frame wich stores hash count for every tweet
        key_list = []
        occurence_counter = []

        loader = ld.Loader(self.size)

        for tweet in self.tweets:
            list = re.findall(patterns[key], tweet)

            if list:
                list = [hash.lower() for hash in list]  # changes hash text to lowercase to avoid case sensivity
                occurence_counter.append(len(list))
                for ele in list:
                    counter = 0
                    if len(ele) != 1:
                        for tag in key_list:
                            if ele == tag[0]:
                                tag[1] += 1
                                counter = 1
                        if counter == 0:
                            key_list.append([ele, 1])
            else:
                occurence_counter.append(0)

            loader.loading()

        sorted_key_list = sorted(key_list, key=lambda x: x[1], reverse=True)
        sorted_key_list = pd.DataFrame(sorted_key_list)

        return sorted_key_list, occurence_counter


    def tweets_len(self): #returns data frame tweet length

        f = lambda x: len(x) # function to get length of every tweet
        data_tweet_len = self.tweets.apply(f)
        data_tweet_len.name = 'Tweet Length'

        return  data_tweet_len

