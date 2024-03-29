# Day 37 - Habit Tracking Project: API Post Requests & Handlers

- We have been using the `.get()` method from `requests` up until this point, but there are [other](https://requests.readthedocs.io/en/latest/api/) methods as well
    + `reuests.get()` - used to retrieve data from an external service (API)
    + `requests.post()` - used to give the API endpoint a piece of data. Such as saving a piece of data to Google sheets
    + `requests.put()` - used to update a piece of data on an external service (API). For example updating values in a spreadsheet on google sheets
    + `requests.delete()` - used to delete a piece of date on an external service (API)

- Today we will be making a habit tracker using the [API](https://docs.pixe.la/) for [Pixela](https://pixe.la/) utilizing 
- Looking at their API documentation, the first thing we need to do is create a user using `.post()`
- We'll store all of our user parameters in a JSON 
```python
import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "1234556745746",
    "username": "my_username",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
# Print response text
print(response.text)
```

- Now when we run that code we get back `{"message":"Success. Let's visit https://pixe.la/@my_username , it is your profile page!","isSuccess":true}` telling us that our user was created
- Next we need to create a graph definition on pixela
- The main difference when we are creating the graph is the authentication requires you to send it via HTTP Header which is much more secure
- You can think about the header as the part of the message that contains your authentication information and other information that doesn't change separate from the actual message

```python
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Python Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
```
- Now if we go to https://pixe.la/v1/users/my_username/graphs/graph1.html we can see that our graph was created
- Next we'll update our graph by [posting](https://docs.pixe.la/entry/post-pixel) a pixel
- Looking at the documentation, one of the requirements is a string with the date for your pixel post. To get the current date as a string we'll import `datetime`, then we'll set a variable to `datetime.now()` and finally we'll set another variable to `thatvariable.strftime("%Y%m%d")` to get the current date as a string
```python
import datetime as dt

# Get current date and time and then get format current date as a string
time = dt.datetime.now()
time_string = time.strftime("%Y%m%d")
print(time_string)

# Set pixel post endpoint url
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}
# JSON data for post
pixel_data = {
    "date": time_string,
    "quantity": "1.5",
}
# Post request
pixel_request = requests.post(url=pixel_post_endpoint, headers=headers, json=pixel_data)
print(pixel_request.text)
```

- Doing a put (update) is fairly simple
```python
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{time_string}"
pixela_update_json = {
    "quantity": "2.5"
}

pixel_update_request = requests.put(url=pixel_update_endpoint, headers=headers, json=pixela_update_json)
print(pixel_update_request.text)
```
- A delete on pixela is even more simple since all we need is the endpoint and headers
```python
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{time_string}"

pixel_delete_request = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(pixel_delete_request.text)
```
## Day 37 - [Code Challenge](https://github.com/TroyCaywood/Python/blob/main/100%20Days%20of%20Code/CodeChallenges/Day-37/main.py) - Pixela Habit Tracker - don't click until you've finished the lesson
