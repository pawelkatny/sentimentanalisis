import re
import pandas as pd
from patterns import patterns_list #regex patterns list
import Loader as ld  # prints current progress


class InitialAnalysis():
    patterns = patterns_list

    def __init__(self, data):
        self.data = data
        self.tweets = data['Tweet']
        self.size = len(data)

    def occurence_counter(self, key):  # emots, hash counter - returns descending sorted array
                                        # and panda data frame wich stores hash count for every tweet
        def create_data_frame(sorted_arr):
            data_frame_sorted = pd.DataFrame(sorted_arr)
            return data_frame_sorted

        key_list = []

        loader = ld.Loader(self.size)

        for tweet in self.tweets:
            list = re.findall(patterns_list[key], tweet)
            list = [hash.lower() for hash in list] #changes hash text to lowercase to avoid case sensivity

            if list:
                for ele in list:
                    counter = 0
                    if len(ele) != 1:
                        for tag in key_list:
                            if ele == tag[0]:
                                tag[1] += 1
                                counter = 1
                        if counter == 0:
                            key_list.append([ele, 1])

            loader.loading()

        sorted_key_list = sorted(key_list, key=lambda x: x[1], reverse=True)

        return create_data_frame(sorted_key_list)


    def tweets_len(self): #returns data frame tweet length

        f = lambda x: len(x) # function to get length of every tweet
        data_tweet_len = self.tweets.apply(f)
        data_tweet_len.name = 'Tweet Length'

        return  data_tweet_len


    def append_data_frame(self, array, array_name): #appends specific data frame

        append_data_frame = self.data
        append_data_frame.insert(len(append_data_frame.columns), array_name, array)

        return append_data_frame