import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
alphavantage_api_key = "12341543543643765"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": alphavantage_api_key
}


# Get stock data from alphavantage and save the Time Series (Daily) key as stock_data
response = requests.get(url=STOCK_ENDPOINT, params=alpha_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

# Convert stock data dictionary to a list to make it easier to work with, keeping only the values.
stock_data_list = [value for (key, value) in stock_data.items()]

# Get yesterday's stock data from index 0
yesterday = stock_data_list[0]

# Get yesterday's closing price from idex 4. close
yesterday_closing_price = yesterday["4. close"]

# Do the same for the day before yesterday in index 1
day_before_yesterday = stock_data_list[1]
day_before_closing_price = day_before_yesterday["4. close"]

# Get difference by taking yesterday's closing price minus day before closing price
pos_difference = float(yesterday_closing_price) - float(day_before_closing_price)

# Create up or down emojis based on difference
up_down = None
if pos_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Get the percentage change by taking the difference divided by yesterday's closing price and then multiply by 100
percent_diff = round((pos_difference / float(yesterday_closing_price)) * 100)

# If percent change is greater than 5 percent
if abs(percent_diff) > .8:
    NEWS_API_KEY = "12341543645657"
    NEWS_PARAMETERS = {
        "q": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API_KEY,
    }
    news_get = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_data = news_get.json()

    # Get articles from news_data json
    articles = news_data["articles"]

    # Slice articles in to the first 3 results
    first_3_articles = articles[:3]

    # Create new list with just headline and description from first 3 articles
    headlines = [f"{STOCK_NAME}: {up_down}{percent_diff}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in first_3_articles]

    # Twilio
    account_sid = "1243124125"
    auth_token = "1231432531"

    # Send a message with each article
    for item in headlines:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{item}",
            from_="+1234567",
            to="+12345567"
        )
