import tweepy
import csv
import random
import os

def reply():
    # authentication based on https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f
    # Authenticate to Twitter
    api_key = os.environ['api_key']
    api_key_secret = os.environ['api_key_secret']
    access_token = os.environ['access_token']
    access_token_secret = os.environ['access_token_secret']
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    twt = api.search(q="@prequelmemebot1")

    #list of specific strings we want to check for in Tweets
    t = ['Hello There!',
        'Hello there!',
        'Hello There!!!',
        'Hello there!!!',
        'Hello, There!',
        'Hello, there!']

    #print(twt)
    for s in twt:
        #print(s.text)
        for i in t:
            #print(i)
            #print(s.text)
            if '@prequelmemebot1 ' + i == s.text:
                sn = s.user.screen_name
                m = "General @%s. You are a bold one." % (sn)
                print(m)
                try:
                    s = api.update_status(m, s.id)
                except tweepy.error.TweepError as e:
                    print(e)

if __name__ == '__main__':
    reply()
