import reddit_scrape
import reddit_analysis

stocks_list = ['msft', 'tsla', 'aapl', 'amzn', 'googl', 'goog', 'brk.b', 'nvda', 'meta', 'unh']
subreddit_list = ['wallstreetbets', 'stocks', 'dividends', 'ValueInvesting']
reddit_scrape.scrape_data(stocks_list, subreddit_list, limit_per_subreddit=20)
reddit_analysis.output_sentiment(stocks_list)