import tweepy
import csv
import random
import re
import os

def main():
	# authentication based on https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f
	# Authenticate to Twitter
	api_key = os.environ['api_key']
	api_key_secret = os.environ['api_key_secret']
	access_token = os.environ['access_token']
	access_token_secret = os.environ['access_token_secret']
	auth = tweepy.OAuthHandler(api_key, api_key_secret)
	auth.set_access_token(access_token, access_token_secret)

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
	firstLines[chosenLineIndex][0] = re.sub(r'%NAME%', fullNames[char2], firstLines[chosenLineIndex][0])
	tweet += firstLines[chosenLineIndex][0] + '\n\n'

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

	api.update_status(tweet)

if __name__ == '__main__':
	main()
