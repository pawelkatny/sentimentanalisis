import re
import pandas as pd
import numpy as np
from patterns import patterns_list
import Loader as ld  # prints current progress


class RawAnalysis():
    patterns = patterns_list

    def __init__(self, data):
        self.data = data
        self.tweets = data['Tweet Content']
        self.size = len(data)

    def occurence_counter(self, key):  # emots, hashes counter - returns descending sorted array
                                        # and panda data frame with stores hash count for every tweet
        # def create_data_frame()

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

        # data_key_list = pd.DataFrame()
        #
        # data_key_list.append()
        return sorted_key_list

