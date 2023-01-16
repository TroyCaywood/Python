import requests
import datetime as dt


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
alphavantage_api_key = "A1SDKX1W37A2Z09X"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": alphavantage_api_key
}

# year = dt.date.today().year
# month = dt.datetime.today().month
# day = dt.datetime.today().day
#
# today_list = [year, month, day]
# today = "-".join(str(today_list))
#print(today)

response = requests.get(url=STOCK_ENDPOINT, params=alpha_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]


yesterday = stock_data_list[0]
yesterday_closing_price = yesterday["4. close"]

day_before_yesterday = stock_data_list[1]
day_before_closing_price = day_before_yesterday["4. close"]

pos_difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))
percent_diff = (pos_difference / float(yesterday_closing_price)) * 100
print(percent_diff)

if percent_diff > 5:
    

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").




#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

