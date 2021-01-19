import tweepy

# Make an extremely basic tweet, based on https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f
# Note: actually keys will be different from code on GitHub to protect the Twitter account's privacy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("j61yE6eUNZsVtNM2RKP3yPcr5", 
    "sYHRbVuYNdnPI3g34HygHh0gk604RfGjCdIpEcTOh08zNIg9dY")
auth.set_access_token("1308162909965443073-ZIAawyZNY97l5ZxArCYaooVXCwVH7p", 
    "qKDZpiIVKZkzplxRjCOgPid6ylPOAHGkCzonQuSYeDLqH")

api = tweepy.API(auth)

api.update_status('Hello there')

# API key: j61yE6eUNZsVtNM2RKP3yPcr5
# API key secret: sYHRbVuYNdnPI3g34HygHh0gk604RfGjCdIpEcTOh08zNIg9dY
# Access token: 1308162909965443073-ZIAawyZNY97l5ZxArCYaooVXCwVH7p
# Access token secret: qKDZpiIVKZkzplxRjCOgPid6ylPOAHGkCzonQuSYeDLqH
# Bearer token: AAAAAAAAAAAAAAAAAAAAACunLwEAAAAAG3Q2Fz83LpsSeHGTr1YlBPI%2Bvl8%3DV5k949LH1CQZiE2dGvBk0GmpZmSpK36Dw2b1xZ8IhzJH3pcOr8