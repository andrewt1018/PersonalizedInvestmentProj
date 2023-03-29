import snscrape.modules.twitter as sntwitter
import pandas as pd
import time

query = "$MSFT lang:en until:2023-03-10 since:2023-03-04"
tweets = []
limit = -1

start = time.time()

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    tweets.append([str(tweet.date), str(tweet.user), str(tweet.renderedContent)])

tweets_df = pd.DataFrame(tweets, columns=['Date', 'User', 'Content'])
print(tweets_df)

end = time.time()
print("Time elapsed: ", end - start)

tweets_df.to_csv("Twitter_data.csv")