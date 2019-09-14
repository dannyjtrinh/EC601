import tweepy
import sys


f = open(sys.argv[1])
key_list = f.readlines()
f.close()

auth = tweepy.OAuthHandler(key_list[0].strip(), key_list[1].strip())
auth.set_access_token(key_list[2].strip(), key_list[3].strip())

api = tweepy.API(auth)

new_tweets = api.user_timeline(screen_name = "Google",count=15)
for results in new_tweets:
    print results
