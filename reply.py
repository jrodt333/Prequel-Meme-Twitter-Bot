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
twt = api.search(q="Hello There!")

#list of specific strings we want to check for in Tweets
t = ['Hello There!',
    'Hello There!',
    'Hello There!!!',
    'Hello There!!!',
    'Hello, There!',
    'Hello, There!']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "General @%s Hahahaha... You are a bold one." % (sn)
            s = api.update_status(m, s.id)