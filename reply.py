import tweepy
import csv
import random

# authentication based on https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f
# Note: actually keys will be different from code on GitHub to protect the Twitter account's privacy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("j61yE6eUNZsVtNM2RKP3yPcr5", 
    "sYHRbVuYNdnPI3g34HygHh0gk604RfGjCdIpEcTOh08zNIg9dY")
auth.set_access_token("1308162909965443073-ZIAawyZNY97l5ZxArCYaooVXCwVH7p", 
    "qKDZpiIVKZkzplxRjCOgPid6ylPOAHGkCzonQuSYeDLqH")
api = tweepy.API(auth)
#twt = api.search(q="Hello There!")
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
