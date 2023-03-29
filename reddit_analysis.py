import numpy as np
from textblob import TextBlob
import pandas as pd


def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity


def get_polarity(text):
    return TextBlob(text).sentiment.polarity


def calculate_sentiment_score(subjectivity, polarity) -> float:
    return float(subjectivity + 1) * polarity


def output_sentiment(stocks_list):
    for stock in stocks_list:

        filename = str(stock + ".csv")
        reddit_df = pd.read_csv(filename)
        subjectivities = []
        polarities = []
        for submission_comments in reddit_df["Comments"]:
            comments = submission_comments.split(";;")
            subjectivity = 0
            polarity = 0
            counter = 0
            for comment in comments:
                if "" in comment:
                    counter = counter + 1
                    subjectivity = subjectivity + get_subjectivity(comment)
                    polarity = polarity + get_polarity(comment)
            if counter == 0:
                subjectivity = None
                polarity = None
            else:
                subjectivity = float(subjectivity) / counter
                polarity = float(polarity) / counter

            subjectivities.append(subjectivity)
            polarities.append(polarity)

        reddit_df["Subjectivity"] = subjectivities
        reddit_df["Polarity"] = polarities

        print("For", filename)
        print("Polarity summed: ", np.average(reddit_df["Polarity"]))
        print("Sentiment score: ", calculate_sentiment_score(np.average(reddit_df['Subjectivity']),
                                                             np.average(reddit_df['Polarity'])))
