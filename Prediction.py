from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd

class Prediction():

    def __init__(self, text_vectors, sentiments_score):
        self.text_vectors = text_vectors
        self.sentiments_score =  sentiments_score

    def predict_sentiment(self):
        x_train, x_test, y_train, y_test = train_test_split(self.text_vectors, self.sentiments_score,
                                                                            test_size=0.2, random_state=1)
        forest = RandomForestClassifier(n_estimators=1000, random_state=None)

        forest.fit(x_train, y_train)
        x_pred  = forest.predict(x_test)

        acc_score = accuracy_score(y_test, x_pred)

        return acc_score, forest.predict(self.text_vectors)