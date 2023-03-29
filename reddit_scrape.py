# Import libraries
import praw
import pandas as pd
pd.set_option("display.max_columns", 10)
pd.set_option('display.width', 400)

# python src/subreddit_downloader.py stocks --reddit-id 3yuWZlunJ7qtpdya11yxMg --reddit-secret
# kobRwlEE03bnjVtRtj3joqs4mtFbmg --reddit-username huski8101 --batch-size=500 --laps 1 --debug --utf-after


def scrape_data(stocks_list, subreddit_list, limit_per_subreddit):
    for stock in stocks_list:
        # Using praw to get the subreddit
        reddit = praw.Reddit(client_id="3yuWZlunJ7qtpdya11yxMg",  # your client id
                             client_secret="kobRwlEE03bnjVtRtj3joqs4mtFbmg",  # your client secret
                             user_agent="App")  # your user agent

        submissions_pd = pd.DataFrame()

        for sub in subreddit_list:
            subreddit = reddit.subreddit(sub)
            counter = 0

            for submission in subreddit.search(query=stock, sort="new", time_filter="week"):
                submissions_dict = {"Subreddit": [], "Title": [], "Flair": [], "Post Text": [], "Post URL": [], "Comments": ""}
                if counter == limit_per_subreddit:
                    break
                # Subreddit the submission belongs to
                submissions_dict["Subreddit"].append(submission.subreddit.display_name)
                # Title of each post
                submissions_dict["Title"].append(submission.title)
                # Flair of each post
                submissions_dict["Flair"].append(submission.link_flair_text)
                # Text inside a post
                submissions_dict["Post Text"].append(submission.selftext)
                # URL of each post
                submissions_dict["Post URL"].append(submission.url)

                comments = []
                submission.comments.replace_more(limit=0)

                for comment in submission.comments:
                    if comment.stickied:
                        continue
                    comments.append(comment.body)

                submissions_dict["Comments"] = ";;".join(comments)
                submissions_pd = pd.concat([submissions_pd, pd.DataFrame(submissions_dict)], ignore_index=True)
                counter = counter + 1

        print(submissions_pd.shape)
        print(submissions_pd.loc[:, ["Subreddit", "Title", "Flair", "Comments"]])
        to_file = str(stock + ".csv")
        submissions_pd.to_csv(to_file)
