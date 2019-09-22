import tweepy


class twitter_scrapper():

    def __init__(self, path):
        f = open(path)
        key_list = f.readlines()
        f.close()
        
        auth = tweepy.OAuthHandler(key_list[0].strip(), key_list[1].strip())
        auth.set_access_token(key_list[2].strip(), key_list[3].strip())
        
        self.api = tweepy.API(auth)

    def search_twitter(self, username, product):
        retweet_filter='-filter:retweets'
        search_words = "#"+product+retweet_filter
        tweet_list = []
        
        # Collect tweets based on product only
        tweets = tweepy.Cursor(self.api.search,
                               q=search_words,
                               lang="en",
                               since=None).items(500)

        # Filter tweets
        for tweet in tweets:
            filt = "".join(tweet.text.lower().split())
            if(filt.find("".join(product.lower().split())) != -1):
                tweet_list.append(tweet.text)

        # Collect tweets from username
        search_words = "@"+username+retweet_filter

        tweets = tweepy.Cursor(self.api.search,
                               q=search_words,
                               lang="en",
                               since=None).items(1000)
         
        for tweet in tweets:
            filt = "".join(tweet.text.lower().split())
            if(filt.find("".join(product.lower().split())) != -1):
                tweet_list.append(tweet.text)
        
        return tweet_list

    
