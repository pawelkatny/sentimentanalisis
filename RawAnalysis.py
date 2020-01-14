import re
import pandas as pd
import numpy as np
from patterns import patterns_list #regex patterns list
import Loader as ld  # prints current progress


class RawAnalysis():
    patterns = patterns_list

    def __init__(self, data):
        self.data = data
        self.tweets = data['Tweet']
        self.size = len(data)

    def occurence_counter(self, key):  # emots, hashes counter - returns descending sorted array
                                        # and panda data frame with stores hash count for every tweet
        def create_data_frame(sorted_arr):
            data_frame_sorted = pd.DataFrame(sorted_arr)
            data_sum = data_frame_sorted.sum(numeric_only=True)
            return (data_frame_sorted, data_sum.at[1])

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


    def tweets_len(self):
        loader = ld.Loader(self.size)
        arr_len = np.array([])
        for tweet in self.tweets:
            arr_len = np.append(arr_len, len(tweet))
            loader.loading()
        data_arr_len = pd.DataFrame(arr_len, columns=['Tweet text length'])
        data_sum_len = data_arr_len.sum(numeric_only=True)

        return data_arr_len, data_sum_len.at['Tweet text length']

    def append_data_frame(self, array):
        data_frame = self.data
        data_frame.insert(5, 'Tweet Length', array)

        return data_frame, data_frame.describe()