import requests, json, dotenv, os
from datetime import datetime

from elementsExtraction import *
from sentDetection import *
from visualDepiction import *

if __name__=='__main__':

	# Loads variables from an .env file
	dotenv.load_dotenv()
	apiKey = os.environ.get("NEWS_API_KEY")

	# User input	
	while True:
		try:
			searchElement = input("\n Enter the topic: ")
			if searchElement.strip() == "":
				raise ValueError
			break
		except ValueError:
			print("\n Warning: A topic to be searched is needed.\n")
	while True:
		try:
			timeType = int(input(" Choose a time period by typing 1 or a date by typing 2: "))
			if timeType not in [1,2]:
				raise ValueError
			break	
		except ValueError:
			print("\n Warning: Only 1 or 2 permitted as input.\n")
	while True:
		try:
			if timeType==1:
				startDate = input(" Enter the start date in the format dd.mm.yyyy: ")
				fromValue = datetime.strptime(startDate, "%d.%m.%Y").date()
				lastDate = input(" Enter the last date in the format dd.mm.yyyy: ")
				toValue = datetime.strptime(lastDate, "%d.%m.%Y").date()
			else:
				singleDate = input(" Enter the date in the format dd.mm.yyyy: ")
				fromValue = datetime.strptime(singleDate, "%d.%m.%Y").date()
				toValue = datetime.strptime(singleDate, "%d.%m.%Y").date()
			break
		except ValueError:
			print("\n Warning: Invalid date format. Please enter a date in the format dd.mm.yyyy.\n")

	# Creating url and parameters for API request
	url='https://newsapi.org/v2/everything?'
	parameters={
		'q': searchElement, # query phrase
    	'pageSize': 20,  # maximum is 100
	    'sortBy' : 'popularity', # order of articels
    	'apiKey': apiKey, # your own API key
		'from' : fromValue,
		'to' : toValue,
		'language' : 'en'
	}
	# Additional parameter: qintitle, sources, domains, sort_by, page, page_size

	# API request for news stories
	response = requests.get(url, params=parameters)
	response_json = response.json()
	newsStories = json.loads(response.text)

	# User input to choose what information to retrieve
	print("\n What information do you want to retrieve? : \n 1. See international news. \n 2. See sentiment value for international news. \n 3. See average sentiment for now. \n")
	while True:
		try:
			check = input(" Enter the number: ")
			if int(check) < 1 or int(check) > 3:
				raise ValueError
			break	
		except ValueError:
			print("\n Warning: Only 1, 2 or 3 permitted as input.\n")

	print("\n")

	# Perform different actions based on user input
	for x in range(1,3):
		if check=='1':
			listNews(newsStories)
		elif check=='2':
			numbers, sentVal = sentimentAnalysis(newsStories)
		else:
			avgSentVal = averageSentiment(newsStories)

	# Display plot of sentiment analysis if option 2 was chosen
	if check== '2':
		buildPlot(numbers, sentVal, searchElement, fromValue, toValue)

	# Display average sentiment if option 3 was chosen
	if check== '3':
		avgSentiment = findSentiment(avgSentVal)
		print(" Average Sentiment now is: " + avgSentiment + ": " + str(round(avgSentVal, 5)))