# News-Sentiment-Analysis
The program utilizes the News API to retrieve news stories related to a user-specified topic within a specified time frame. It then performs sentiment analysis on the retrieved news stories and provides the user with various options for displaying the information.

## Prerequisites
This program requires a valid API key from the News API website (https://newsapi.org/). The API key should be stored in an .env file in the same directory as the Python script with the key name NEWS_API_KEY.

The required Python modules for running this program are:

- requests (pip installment required)
- json
- dotenv (pip installment required)
- os
- datetime
- TextBlob (pip installment required)

## How to use the program
1. Run the Python script.
2. Enter a topic you want to search for.
3. Choose a time period by typing 1 or a date by typing 2.
4. Enter the date(s) in the format dd.mm.yyyy.
5. Choose what information to retrieve from the news stories by typing 1, 2, or 3.
6. If you chose option 1, the news and the corresponding description will be displayed. 
7. If you chose option 2, a plot of the sentiment analysis will be displayed.
8. If you chose option 3, the average sentiment of the retrieved news stories will be displayed.

## Acknowledgments
This program was created using the News API (https://newsapi.org/) and TextBlob (https://textblob.readthedocs.io/en/dev/).