import tweepy
import sys


class twitter_scrapper():

    def __init__(self, path):
        f = open(path)
        key_list = f.readlines()
        f.close()
        
        auth = tweepy.OAuthHandler(key_list[0].strip(), key_list[1].strip())
        auth.set_access_token(key_list[2].strip(), key_list[3].strip())
        
        self.api = tweepy.API(auth)

    def search_twitter(self, username, product):
        search_words = "#"+product
        date_since = "2018-1-1"
        
        # Collect tweets
        tweets = tweepy.Cursor(self.api.search,
                               q=search_words,
                               lang="en",
                               since=date_since).items(400)

        tweet_list = []
        # Iterate and print tweets
        for tweet in tweets:
            tweet_list.append(tweet.text)

        return tweet_list

    
