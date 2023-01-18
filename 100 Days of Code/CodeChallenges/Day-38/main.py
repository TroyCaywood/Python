import requests
import datetime
import os

APP_KEY = os.environ["APP_KEY"]
APP_ID = os.environ["APP_ID"]
USER_ID = os.environ["USER_ID"]

BEARER_TOKEN = os.environ["BEARER_TOKEN"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

# Headers for nutritionix post
HEADERS = {
    "x-app-key": APP_KEY,
    "x-app-id": APP_ID,
    "x-remote-user-id": USER_ID
}

# JSON for nutritionix post
exercise_json = {
    "query": f"{input('What exercises did you do today and for how long? ')}",
    "gender": "male",
    "weight_kg": 73.03,
    "height_cm": 177.8,
    "age": 38
}

exercise_post_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=HEADERS, json=exercise_json)
exercise_post_response.raise_for_status()
result = exercise_post_response.json()
print(result)

# Create date and time strings
today_now = datetime.datetime.now()
today_time = today_now.strftime("%H:%M")
today_now_str = today_now.strftime("%d/%m/%Y")

# Create parameters for sheetly post from each exercise submitted
for exercise in result["exercises"]:
    sheetly_params = {
        "workout": {
            "date": today_now_str,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }

    headers = {
        "Authorization": BEARER_TOKEN
    }

    sheetly_response = requests.post(url=SHEET_ENDPOINT, json=sheetly_params, headers=headers)
    sheetly_response.raise_for_status()
    print(sheetly_response.text)