import pandas as pd

#Functions that can be used globally


def append_to_data_frame(data, array_name, array):
        new_data = data
        new_data.insert(len(data.columns), array_name, array)

        return new_data