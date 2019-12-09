import mysql.connector


class mysql_class():

    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mydatabase"
        )
        self.mycursor = self.mydb.cursor()

    def insert_tweet(self, tweet_info_list):
        sql = "INSERT INTO tweets (username, product, tweet, score) VALUES (%s, %s, %s, %s)"
        val = (tweet_info_list[0], tweet_info_list[1], tweet_info_list[2], tweet_info_list[3])
        #self.mycursor.execute(
        #    "CREATE TABLE tweets (id INT AUTO_INCREMENT PRIMARY KEY,"+\
        #    "username VARCHAR(255),"+\
        #    "product VARCHAR(255),"+\
        #    "tweet VARCHAR(255),"+\
        #    "score VARCHAR(255))")
        self.mycursor.execute(sql, val)
        self.mydb.commit()
