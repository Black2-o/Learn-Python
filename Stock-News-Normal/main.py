import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
APIKEY = "E635NLF9WMXTGT26"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "03c56195707745c8bf9d235491d0757c"


# Day Find:




    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

params = {
    "apikey": APIKEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME
}

response = requests.get(STOCK_ENDPOINT, params=params)

data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


# print(yesterday_closing_price)
# print(day_before_yesterday_closing_price)


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))


parcentige = (difference / float(yesterday_closing_price)) * 100


if parcentige > 3:
    news_parems = {
        "apiKey": NEWS_API,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parems)
    articles = news_response.json()["articles"]
    three_articles = articles[:1]
    print(three_articles)

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

