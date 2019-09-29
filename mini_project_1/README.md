# Flop or Not

Users will be able to enter the Twitter username of the company they are interested in along with their product. From there, the application will be able to determine whether the product was a flop. This product is intended for both companies and consumers. Consumers will be able to determine if the product they are interested in is good. Companies on the other hand benefit from the same query. The application will be able to give a detailed breakdown as to why were the results given as such.

But how does it work? Obtaining the two inputs from the user, tweets will be grabbed at various times to obtain adequate information for prediction. There will be some sort of algorithm to determine whether the product is new or old. From there, the application will try to dive deeper using Google Cloud APIs to determine the main cause for the results given to the user.  Finally, all that information is aggregated and arranged in a form easily digestible by the user.

While this application is intended for companies and their products, this target could be interpreted in various always. As a result, the same user can obtain information from a popular movie reviewer and determine if many individuals like a movie that just came out. The possibilities for Flop or Not are endless!

# Architecture

<img src="https://github.com/djtrinh/EC601/blob/master/mini_project_1/docs/Flop%20or%20Not%20Arch.PNG">

# How to Run?
This application requires PYQT4, Tweepy, Google Natural Language API and Python 2



Please make sure all APIs have been installed before running the program. To run the program, run the script called run.sh. Twitter key paths must be specified in the run.sh. The file should be of the following format:

```python
[auth]
consumer_key = ****
consumer_secret = ****
access_token = ****
access_secret = ****
```

# User Stories

-I as a user should be greeted with a simple and elegant interface

-I as a user should be able to enter any Twitter handle and product

-I as a user should have a prompt when I have entered an invalid Twitter handle

-I as a user should be given the result of my product search if it was a hit or not

-I as a user should be given the detailed results of my product search, specifically, why it was scored the way it was

-I as a user should be able to save my results to a file

# Backlog

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

# Testing

The user experience is key for this application. As a result, the user must be able to enter a Twitter account and product name. Their top tweets and worst tweets must be listed in the results window along with the average sentiment score. The color of the UI also changes with respect to the sentiment score. Green indicates a great product, yellow good, orange mediocre, and red is a flop.

<img src="https://github.com/djtrinh/EC601/blob/master/mini_project_1/docs/gui_search.PNG">

When a user enters just the product, a dialog must be displayed letting the user know that better results could be displayed with a username entered.

<img src="https://github.com/djtrinh/EC601/blob/master/mini_project_1/docs/notice.PNG">

All GUI elements must be functional. The user should not be able to break the program at anytime. Therefore, I spent a good amount of time being a monkey to try and break the program.

<img src="https://github.com/djtrinh/EC601/blob/master/mini_project_1/docs/about.PNG">

# Lessons Learned

With this project, I have learned that are tons of information out there. As a result of this there is a ton of bad information as well. Filtering out this information is key to getting accurate results. Creating the GUI is both fun and frustrating at the same time. NLP was where all the fun really happened but there were too many limits with the free Twitter developer account.

What I could have done better was actually have someone look into a database for this project. As a one man team, creating a GUI, integrating both Google Natural Language and Twitter APIs along with data preprocessing, there was a mountain of work to be done with so little time. I also wanted to create a better spam filter. This would require machine learning to predict whether or not the tweet is spam instead of removing tweets based off spam keywords. Also, instead of discarding tweets with images, I want to do image processing to further improve tweet and sentiment score results.

In the future, I will modularize my code better. It has to start from the beginning and that includes good directory structures, code skeletans, etc.
