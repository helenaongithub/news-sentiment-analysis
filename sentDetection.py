from textblob import TextBlob             
from elementsExtraction import *
from visualDepiction import *

# Sentiment analysis on a given set of news stories
def sentimentAnalysis(news):
  lists = []
  stories = newsGrabber(news)
  titles = [article["title"] for article in news["articles"]]
  newsPaper = dict(zip(titles,stories))
  sent, sentVal = analysisTool(newsPaper)
  lists, totalSent = listCreater(newsPaper, titles, sent, sentVal, lists)
  for i in range(len(newsPaper)):
    print(lists[i])
  numbers = [i + 1 for i in range(len(lists))]
  return numbers, sentVal

# Calculate the average sentiment score for a given set of news stories 
def averageSentiment(news):
  lists = []
  stories = newsGrabber(news)
  titles = [article["title"] for article in news["articles"]]
  newsPaper = dict(zip(titles,stories))
  sent, sentVal = analysisTool(newsPaper)
  lists, totalSent = listCreater(newsPaper, titles, sent, sentVal, lists)
  avgSent = totalSent / len(titles)
  return avgSent
     
# Analyze the sentiment of a given piece of text using TextBlob and return sentiment and polarity score
def analysisTool(dataDic):
  sent = []
  sentVal = []
  for newsStory in list(dataDic.values()):
    analysis = TextBlob(newsStory)
    sentiment = findSentiment(analysis.sentiment.polarity)
    polScore = round(analysis.sentiment.polarity, 5)
    sentVal.append(polScore)
    sent.append(sentiment)
  return sent, sentVal

# Determine the sentiment category based on the polarity score
def findSentiment(val):                                                                                                               
  if val<=0.1 and val>-0.1:
      return 'Neutral'
  elif val>0.1:
      return 'Positive'
  else:
      return 'Negative'

# Create a list of news stories along with their sentiment and polarity scores, and calculate the total polarity score
def listCreater(newsPaper, titles, sent, sentVal, lists):
  totalSent = 0
  for i in range(len(newsPaper)):
    sas = titles[i] + ' : ' + sent[i]+ ' : ' + str(sentVal[i])
    # Sums up scores
    totalSent+=sentVal[i]
    lists.append(sas)
    lists= [x.replace('\n', '') for x in lists]
  return lists, totalSent