import re
from google.cloud import language
from google.cloud.language import enums


def analyze(username, product, sentence_list, db, sql):
    score_list = []
    neg_list = []
    pos_list = []
    sent_list = []
    tweet_list = []
    
    for i in sentence_list:
        if(i.count("https://") == 1):
            url = i.find("https")
        #print(i+"\n\n")
            tweet = i[:url-1].strip()
            url_link = i[url:].strip()
            if(len(url_link.split()) == 1):
                tweet_list.append((tweet, url_link))

    tweet_list = remove_dups(tweet_list)
    tweet_list_filt = filter_tweets(tweet_list)

    client = language.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.HTML

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    #language = "en"
    
    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    for i, tweet in enumerate(tweet_list_filt):
        document = {"content": tweet[0], "language": "en", "type": type_}
        response = client.analyze_sentiment(document, encoding_type=encoding_type)

        score = float(response.document_sentiment.score)
        if(score != 0.0):
            score_list.append(score)
            sent_list.append(tweet_list[i][0]+"\n"+tweet[1].split()[0])
            
            if(score < 0.0):
                neg_list.append(score)
            else:
                pos_list.append(score)

            db.insert_tweet([username, product, tweet[0], score])
            sql.insert_tweet([username, product, tweet[0], score])
            
        
    # Get overall sentiment of the input document
    #print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    #print(
    #    u"Document sentiment magnitude: {}".format(
    #        response.document_sentiment.magnitude
    #    )
    #)
    # Get sentiment for all sentences in the document

    # for sentence in response.sentences:
    #     #print(u"Sentence text: {}".format(sentence.text.content))
    #     #print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
            
        #print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    
    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    #print(u"Language of the text: {}".format(response.language))
    sorted_list = sorted(zip(score_list, sent_list), reverse=True)
    top_tweets = sorted_list[:3] + sorted_list[-3:]

    try:
        neg_avg = sum(neg_list)/len(neg_list)
        pos_avg = sum(pos_list)/len(pos_list)
        avg = (neg_avg+pos_avg)/2.0 #experimenting with averages
        #avg = sum(score_list)/len(score_list)
    except:
        avg = 0
        
    return avg, top_tweets

def remove_dups(tweet_list): 
    new_list = [] 
    for tweet in tweet_list:
        dup = False
        for new_list_tweet in new_list:
            if new_list_tweet[0][0:14] == tweet[0][0:14]:
                dup = True
        if(dup == False):        
            new_list.append((tweet[0], tweet[1]))

    return new_list 

def filter_tweets(tweet_list):
    filt_list = []
    for tweet in tweet_list:
        filt_list.append((' '.join(\
            re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",\
                   tweet[0]).split()), tweet[1]))

    return filt_list
