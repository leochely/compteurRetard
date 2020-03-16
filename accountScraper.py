import twitterscraper as ts
import pandas as pd
import codecs
import json


class AccountScraper:

    def __init__(self, account_name, tweet_file="tweets.json"):
        self.account_name = account_name
        self.tweet_file = tweetFile

    def scrap(self):
        try:
            codecs.open(self.tweetFile, 'r', 'utf-8') as f:
            tweets = json.load(f, encoding='utf-8')
            lastScrap = tweets[-1]["timestamp"][0:10]
        except IOError:
            lastScrap = "2006-01-01"
        list_of_tweets = ts.query_tweets(
            "from:{} since{}".format(self.account, lastScrap))
