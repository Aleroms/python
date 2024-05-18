import requests
import datetime
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_key = os.environ["stock_apikey"]
news_key = os.environ["news_apikey"]

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
stock_params = {
    "function": "TIME_SERIES_Daily",
    "symbol": STOCK,
    "apikey": stock_key
}
news_params = {
    "apiKey": news_key,
    "q": COMPANY_NAME,
    "pageSize": 3
}
deltaThreshold = 5


def didPriceIncrease(day, prev):
    delta = (day - prev) / prev * 100
    return abs(delta) > deltaThreshold


def printNews():
    news_response = requests.get(url=news_endpoint, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    for info in news_data["articles"]:
        print(info["title"])
        print(info["description"])
        print(info["content"])


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday_date = datetime.date.today() - datetime.timedelta(days=1)
dby_date = yesterday_date - datetime.timedelta(days=1)

stock_response = requests.get(url=stock_endpoint, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterdays_close = float(stock_data["Time Series (Daily)"][str(yesterday_date)]['4. close'])
dby_close = float(stock_data["Time Series (Daily)"][str(dby_date)]['4. close'])

if didPriceIncrease(yesterdays_close, dby_close):
    printNews()
printNews()
