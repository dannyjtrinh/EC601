import pymongo


class mongodb():

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["mydatabase"]

    def insert_tweet(self, tweet_info_list):
        mydict = { "username": tweet_info_list[0],
                   "product": tweet_info_list[1],
                   "tweet": tweet_info_list[2],
                   "score": tweet_info_list[3]}
        mycol = self.mydb['tweets']
        mycol.insert_one(mydict)        
        
    def print_col(self, mycol):
        for x in mycol.find():
            print(x)
