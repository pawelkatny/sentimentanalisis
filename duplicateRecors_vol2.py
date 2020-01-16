import pandas as pd


def DeleteDuplicateValues():
  data = pd.read_csv('tweets.csv',names =['Date','Tweet','Language','Retweets','Likes'])

  data.drop_duplicates(subset ="Tweet", 
                     keep = False, inplace = True)

  data.to_csv('tweets_final.csv')

