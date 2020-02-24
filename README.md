# Sentimental analysis
Python sentiment analysis of tweets content for school project.


## Classes overview:

**InitialAnalysis** - initial data analysis
Methods: 
  - occurence_counter()  -  returns descending sorted array
  and panda data frame which stores hash (or any other chosen element) count for every tweet

  - tweets_len() - returns data frame with length of every tweet


**TextProcessing** - cleaning, lemmatizing and vectorizing text
Methods:
  - clean_all_tweets() - removes specials expressions like http, @, #, & and number from every tweet

  - deep_clean_all_tweets() - removes special and single characters, stop words and lemmatize words eventually

  - vectorise() - vectorise text with TFIDF methods using sklearn library


**Sentiment** - uses nltk`s Vader component to compute sentiments (based on “compound” score)

Compound settings:
compound < -0.05: value = 'negative'
compound > 0.05: value = 'positive'
else = ‘neutral’

Methods: 
  - check_sentiment_vader() - applies internal functions on each tweet to compute sentiment value

**Prediction** - uses sklearn and Random Forest Classifier for training model
Methods: 
  - predict_sentiment() - returns predicted values with accuracy score

**Loader** - shows current progress bar in console


## Other modules:

**Functions** - module used to import function that adds array to data frame
**Patterns** - list of regex patterns for text processing
