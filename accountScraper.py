import pandas as pd
import datetime
import GetOldTweets3 as got
import json
import codecs


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


class AccountScraper:

    def __init__(self, account_name, tweet_file="tweets.json"):
        self.account = account_name
        self.tweet_file = tweet_file

    def scrap(self):
        # try:
        #     with codecs.open(self.tweet_file, 'r', 'utf-8') as f:
        #         tweets = json.load(f, encoding='utf-8')
        #         last_scrap = tweets[-1]["timestamp"][0:10]
        # except IOError:
        #     last_scrap = "2006-01-01"

        tweetCriteria = got.manager.TweetCriteria().setUsername("RERB")\
            .setSince("2015-09-10")\
            .setEmoji("unicode")

        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        with codecs.open(self.tweet_file, 'w', 'utf-8') as output:
            json_string = json.dump(
                [ob.__dict__ for ob in tweets], output, default=default)
            print(json_string)
