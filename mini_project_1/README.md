# Flop or Not

Users will be able to enter the Twitter username of the company they are interested in along with their product. From there, the application will be able to determine whether the product was a flop. This product is intended for both companies and consumers. Consumers will be able to determine if the product they are interested in is good. Companies on the other hand benefit from the same query. The application will be able to give a detailed breakdown as to why were the results given as such.

But how does it work? Obtaining the two inputs from the user, tweets will be grabbed at various times to obtain adequate information for prediction. There will be some sort of algorithm to determine whether the product is new or old. From there, the application will try to dive deeper using Google Cloud APIs to determine the main cause for the results given to the user.  Finally, all that information is aggregated and arranged in a form easily digestible by the user.

While this application is intended for companies and their products, this target could be interpreted in various always. As a result, the same user can obtain information from a popular movie reviewer and determine if many individuals like a movie that just came out. The possibilities for Flop or Not are endless!

# How to Run?
This application requires PYQT4, Tweepy, Google Natural Language API and Python 2



Please make sure all APIs have been installed before running the program. To run the program, run the script called run.sh. Twitter key paths must be specified in the run.sh. The file should be of the following format:

[auth]
consumer_key = ****
consumer_secret = ****
access_token = ****
access_secret = ****

### User Stories

-I as a user should be greeted with a simple and elegant interface

-I as a user should be able to enter any Twitter handle and product

-I as a user should have a prompt when I have entered an invalid Twitter handle

-I as a user should be given the result of my product search if it was a hit or not

-I as a user should be given the detailed results of my product search, specifically, why it was scored the way it was

-I as a user should be able to save my results to a file

### Backlog

[X] User interface to accept company name and product

[X] Feed user and product keyword to Twitter API

[X] Arrange the data in a form that is easily digestible by the program/code

[X] Come up with an algorithm to figure out the time period of the product

[X] Obtain more tweets in the form of mentions and etc

[X] Have all that data in a form for the Google API to grab information about

[X] Grab sentiment information from the Google Natural Language API

[X] Determine if is a good product or not

[X] Find out the reason why for the sentiment score

[X] determine in a deeper level as to why the bad/good sentiment based on Google Cloud API information

[X] Aggregate all the information in a digestible format for the user

[X] Display information on the user interface

[X] Display color spectrum based off the product rating

[ ] Use picture information in tweets to enhance sentiment info
