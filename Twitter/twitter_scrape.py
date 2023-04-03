import snscrape.modules.twitter as sntwitter
import pandas as pd
import time
from os import path
from datetime import date, timedelta


def search_twitter(limit=20, words="", language="en", until=date.today(),
                   since=(date.today() - timedelta(days=7))):

    words = words.strip()
    query = words + " lang:" + language + " " + "until:" + str(until) + " since:" + str(since)

    tweets = []
    tweets_limit = limit

    start = time.time()

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == tweets_limit:
            break
        tweets.append([words, str(tweet.date), str(tweet.user), str(tweet.url), str(tweet.renderedContent)])
    tweets_df = pd.DataFrame(tweets, columns=['Symbol', 'Date', 'User', 'URL', 'Content'])
    print(tweets_df)

    end = time.time()
    print("Time elapsed: ", end - start)

    return tweets_df
