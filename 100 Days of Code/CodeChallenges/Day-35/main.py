import requests
import json
from twilio.rest import Client

# API Key for openweather and account_sid for and auth_token for Twilio
api_key = "1234567890"
account_sid = "1234567890"
auth_token = "1234567890"

# Latitude, Longitude, and api endpoint for openweather params
MY_LAT = 48.512940
MY_LONG = 17.302530
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

# Parameters for openweather API call
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

# Get openweather API request
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

# Save API response JSON in weather_data variable
weather_data = response.json()

# Slice returned JSON into 12 entries for 12 hours from 7
weather_slice = weather_data["hourly"][:12]

# Variable to change if raining
will_rain = False

# For loop that takes weather_slice and looks at id key in ["weather"][0]["id"] and if it's less than 700
# change will_rain to true
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# If will_rain is true, authenticate to Twilio, send text message and print message send status.
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="☔️☔️☔️☔️\nBring an umbrella! There is going to be precipitation today!\n☔️☔️☔️☔️",
            from_="+1234567890",
            to="+1234567890"
        )

    print(message.status)
