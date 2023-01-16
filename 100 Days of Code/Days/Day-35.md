# Day 35 - Keys, Authentication, & Environment Variables: Send SMS

- So far we've only been using free APIs, but not all APIs are free. Some must be purchased since a lot of work went into creating the data for them
- You can think of paid APIs as selling data
- A lot of paid APIs provide a free tier for learning or with very small user bases
- The way paid APIs prevent people from abusing their service is by using an **API key** which is like your personal account name and password
- We are going to be using an API key from [open weather](https://openweathermap.org) to create an app that will send an SMS message to us when it's going to rain

## Rain Alert

- To begin, we are going to need to setup our API call to open weather
```python
import requests
import json

api_key = "1234567890"
MY_LAT = 48.646030
MY_LONG = 93.739440
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()

```

- If we `print` our data, we get a huge JSON response with a ton of data
- Using an [online JSON viewer](http://jsonviewer.stack.hu) makes it much eaiser to find what we're looking for
- We want the weather for the next 12 hours. There is a section of the JSON that is a list of dictionaries of weather for the next 48 hours with a dictionary stored in each hour containing the current conditions for that hour
- Since we don't need all the extra forecasts. Let's add the exclude parameter from the API documentation
```python
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
```
- Now we only get back the hourly part of the forecast
- If we look at the API documentation, any weather ID under 700 means there is some type of precipitation
- The exact data we want is in `weather_data["hourly"][range(13)]["weather"][0]["id"]` so lets slice that up further and create a print statement if it's raining
```python
weather_data = response.json()
# Slice weather using range :12 (hour 0-12)

weather_slice = weather_data["hourly"][:12]

# Set boolean for rain condition
will_rain = False

# For loop that goes through each hour of weather_slice and then checks the weather ID code. If the code is under 700 change will_rain to True
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# If will_rain is true print our rain statement
if will_rain:
    print(f"Bring an umbrella! There is going to be precipitation today!")
```

- Now that we are getting the data that we want, let's create a way to send an SMS to our cell phone if it's going to rain
- We will be using the [Twilio](https://www.twilio.com/) API to do this
- Looking at the documentation, we need to `from twilio.rest import Client` first
- Then we'll add our `account_sdi` and `auth_token` from Twilio
- Finally, we'll change our `will_rain` if statement to use Twilio rather than printing adding our Twilio number and test cell number as the recipient

```python
import requests
import json
from twilio.rest import Client

api_key = "1234567890"
account_sid = "1234567890"
auth_token = "1234567890"


MY_LAT = 48.512940
MY_LONG = 17.302530
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]


will_rain = False

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="☔️☔️☔️☔️\nBring an umbrella! There is going to be precipitation today!\n☔️☔️☔️☔️",
        from_="+1234567890",
        to="+1234567890"
    )

    print(message.status)
```
- If we want to automate our code to run at 7 AM every day you can create an account on [python anywhere](https://www.pythonanywhere.com/)
- After creating an account you have to upload your main.py file
- Then for Twilio to work over their proxy server you have to change a few [lines of code](https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/)

## Environment Variables

- Environment variables allow you to separate out where you store secret keys and various other variables away from where your codebase is located either for convenience (such as a client email list for a long program) or security (such as storing secret keys for an API call)
- If you open the python terminal on a project you're working on and type env it will show you all the environment variables
- To save a new environment variable in the terminal type export VARIABLE_NAME=variabledatafromproject
- Then you can `import os` and instead of the value of that variable you exported you'll put variable_name = os.environ.get("ENV_VARIABLE_NAME")
- Doing that will keep your auth tokens etc secret if someone gets the contents of your script
- If you export your auth_token and api_key on python anywhere, you'll need to add export AUTH_TOKEN=20938402398(your token); export API_KEY=20938430298(your key); python3 main.py to the task for it to work correctly
- This is just one example of APIs to play with. [Here](https://apilist.fun) is a list of other APIs to try

