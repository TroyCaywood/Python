import requests
import datetime as dt

USERNAME = "my_username"
TOKEN = "1232141"
GRAPH_ID = "graph1"

# Create User
pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": "1232141",
#     "username": "my_username",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

# Create Graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Python Study Graph",
#     "unit": "Hours",
#     "type": "float",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
time = dt.datetime.now()
time_string = time.strftime("%Y%m%d")
print(time_string)

pixelpost_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_data = {
    "date": time_string,
    "quantity": "1.5",
}

pixel_request = requests.post(url=pixelpost_endpoint, headers=headers, json=pixel_data)
print(pixel_request.text)
