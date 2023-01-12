# Day 33 - API Endpoints & API Parameters - ISS Overhead Notifier

## API - Application Programming Interfaces

- An [API](https://en.wikipedia.org/wiki/API) is a set of commands, functions, protocols, and objects that programmers can use to create software or interact with an exernal system.
- We are going to APIs it to pull live data from websites
- You can think of an API as a menu that tells you what you can do to interact with that external system such as Yahoo weather

#### API Endpoint

- An API endpoint when it comes to a website is usually a URL that tells you where the data you are looking for is stored
- To get data you have to make an **API request** to the API Endpoint. Some API requests require authentication, while others do not
- The vast majority of APIs respond using JSON

#### API Request Example

- Let's make a request to the [ISS current location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) API!
- First we'll need to import the `requests` [library](https://pypi.org/project/requests/)
- Then we create a variable and use `requests.get(url='https://pypi.org/project/requests/')` to create a request
- Then we'll print it and we get back a response code of 200
````python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
````

- But what does response code 200 mean?
- If we look it up [here](https://www.webfx.com/web-development/glossary/http-status-codes/) we can see that 200 means OK meaning our request was successful
    + 1xx codes mean hold on something's happening this is not final
    + 2xx codes mean everything was successful
    + 3xx usually mean you don't have permission
    + 4xx are client error meaning you messed something up in your request
    + 5xx are a server error meaning there is an issue on the other end of the request

- Using our previous example, if we instead `print(response.status_code)` we just get back the status code of Success instead of 200
- We can use the status codes for error handling
```python
if response.status_code == 404:
    raise Exception("That resource does not exist.")

elif response.status_code == 401:
    raise Exception("You are not authorized to access this data.")
```
- Doing it that way would be very time consuming. Instead, we can use the `requests` module's built in `raise_for_status()' method
- If we make a typo in our URL. We'll now get back a 404 error `requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/issnow.json`
```python
import requests

response = requests.get(url="http://api.open-notify.org/issnow.json")
response.raise_for_status()
```
- We can get ahold of the json data for our API request by using `response.json()`

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)
```
- When we print that, we get back the JSON data of `{'iss_position': {'longitude': '100.2344', 'latitude': '2.8622'}, 'message': 'success', 'timestamp': 1673563870}`
- We can work with that data the same way as any other JSON data
- For example, we could assign a variable `longitude` to `data["iss_position"]["longitude"]` to get just the longitude portion of the data

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)
```