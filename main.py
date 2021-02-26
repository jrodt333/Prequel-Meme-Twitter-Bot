import tweepy
import csv
import random
import re

# authentication based on https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f
# Note: actually keys will be different from code on GitHub to protect the Twitter account's privacy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("j61yE6eUNZsVtNM2RKP3yPcr5", 
    "sYHRbVuYNdnPI3g34HygHh0gk604RfGjCdIpEcTOh08zNIg9dY")
auth.set_access_token("1308162909965443073-ZIAawyZNY97l5ZxArCYaooVXCwVH7p", 
    "qKDZpiIVKZkzplxRjCOgPid6ylPOAHGkCzonQuSYeDLqH")

api = tweepy.API(auth)

characters = ['obi', 'anakin', 'palp', 'grievous', 'mace']
fullNames = ['Obi-Wan', 'Anakin', 'Palpatine', 'General Grievous', 'Mace Windu']

char1 = random.randint(0, len(characters)-1)
char2 = char1

while char2 == char1:
	char2 = random.randint(0, len(characters)-1)

tweet = ''

# read csv, from https://www.programiz.com/python-programming/reading-csv-files
firstLines = []
with open('quotes/'+characters[char1]+'_start.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		firstLines.append(row)

tweet += fullNames[char1] + ': '
chosenLineIndex = random.randint(0, len(firstLines)-1)
#if firstLines[chosenLineIndex][1] == 'TRUE':
firstLines[chosenLineIndex][0] = re.sub(r'%NAME%', fullNames[char2], firstLines[chosenLineIndex][0])
tweet += firstLines[chosenLineIndex][0] + '\n\n'  # the T/F part will be handled later

midLines = []
with open('quotes/'+characters[char2]+'_response.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		midLines.append(row)

tweet += fullNames[char2] + ': '
chosenLineIndex = random.randint(0, len(midLines)-1)
midLines[chosenLineIndex][0] = re.sub(r'%NAME%', fullNames[char1], midLines[chosenLineIndex][0])
tweet += midLines[chosenLineIndex][0] + '\n\n'

lastLines = []
with open('quotes/'+characters[char1]+'_response.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		lastLines.append(row)

tweet += fullNames[char1] + ': '
chosenLineIndex = random.randint(0, len(lastLines)-1)
lastLines[chosenLineIndex][0] = re.sub(r'%NAME%', fullNames[char2], lastLines[chosenLineIndex][0])
tweet += lastLines[chosenLineIndex][0]
print(tweet)

#api.update_status(tweet)

# API key: j61yE6eUNZsVtNM2RKP3yPcr5
# API key secret: sYHRbVuYNdnPI3g34HygHh0gk604RfGjCdIpEcTOh08zNIg9dY
# Access token: 1308162909965443073-ZIAawyZNY97l5ZxArCYaooVXCwVH7p
# Access token secret: qKDZpiIVKZkzplxRjCOgPid6ylPOAHGkCzonQuSYeDLqH
# Bearer token: AAAAAAAAAAAAAAAAAAAAACunLwEAAAAAG3Q2Fz83LpsSeHGTr1YlBPI%2Bvl8%3DV5k949LH1CQZiE2dGvBk0GmpZmSpK36Dw2b1xZ8IhzJH3pcOr8