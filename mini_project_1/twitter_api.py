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
        filt='-filter:retweets'
        tweet_list = []

        if(product != ""):
            search_words = "#"+product+filt

            # Collect tweets based on product only
            tweets = tweepy.Cursor(self.api.search,
                                   q=search_words,
                                   lang="en",
                                   since=None).items(250)

            # Filter tweets
            for tweet in tweets:
                tweet_proc = "".join(tweet.text.lower().split())
                if(tweet_proc.find("".join(product.lower().split())) != -1):
                    if(self.spam_checker(tweet_proc) == False):
                        tweet_list.append(tweet.text)

        # Collect tweets from username
        if(username != ""):
            search_words = "@"+username+filt
        
            tweets = tweepy.Cursor(self.api.search,
                                   q=search_words,
                                   lang="en",
                                   since=None).items(500)

            for tweet in tweets:
                tweet_proc = "".join(tweet.text.lower().split())
                
                if(tweet_proc.find("".join(product.lower().split())) != -1):
                    if(self.spam_checker(tweet_proc) == False):
                        tweet_list.append(tweet.text)
                        
        return tweet_list

    def spam_checker(self, string):
        spam_keywords = ["sweepstakes", "contest", "ebay", "sale", "http/1.1",
                         "giveaway", "case", "bestbuy", "walmart", "unlocked",
                         "factory"]
        for word in spam_keywords:
            if(string.find(word) != -1):
                return True

        return False
