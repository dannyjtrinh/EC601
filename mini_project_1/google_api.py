"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
from google.cloud.language_v1 import enums



def analyze(sentence_list):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """
    text_block = ""

    for i in sentence_list:
        text_block = text_block + i + "."
    
    text_content = text_block
    
    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    summ = 0
    num = 0
    
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        if(float(sentence.sentiment.score) != 0.0):
            summ = summ + float(sentence.sentiment.score)
            num = num + 1
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    print("the summ is %f and number of sentences  %f" % (summ, num))
    try:
        avg = summ/num
    except:
        avg = 0
        
    return avg