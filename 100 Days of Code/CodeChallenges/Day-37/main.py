import requests
import datetime as dt

USERNAME = "my_user"
TOKEN = "12379872197"
GRAPH_ID = "graph1"

#-----------------CREATE USER-----------------#

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "1232141",
    "username": "my_username",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
response.raise_for_status()
print(response.text)


#-----------------CREATE GRAPH-----------------#


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


#-----------------POST PIXEL-----------------#

time = dt.datetime.now()
time_string = time.strftime("%Y%m%d")
print(time_string)

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_data = {
    "date": time_string,
    "quantity": "2.5",
}

pixel_request = requests.post(url=pixel_post_endpoint, headers=headers, json=pixel_data)
print(pixel_request.text)

#-----------------UPDATE PIXEL-----------------#

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{time_string}"
pixela_update_json = {
    "quantity": "2.5"
}

pixel_update_request = requests.put(url=pixel_update_endpoint, headers=headers, json=pixela_update_json)
print(pixel_update_request.text)

#-----------------DELETE PIXEL-----------------#

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{time_string}"

pixel_delete_request = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(pixel_delete_request.text)
