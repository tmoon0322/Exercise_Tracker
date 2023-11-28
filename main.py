import requests
import datetime as dt
import os


today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

exercise_endpoint = "v2/natural/exercise"
headers = {
    "x-app-id": os.environ["NUTRITION_APP_ID"],
    "x-app-key": os.environ["NUTRITION_API_KEY"],
    "x-remote-user-id": "0"
}
exercise_config = {
    "query": input("Tell me what exercises you did: "),
    "gender": "male",
    "age": "22",
    "weight_kg": "68.0389",
    "height_cm": "175.26",
}

response = requests.post(url=f"{os.environ['NUTRITION_ENDPOINT']}{exercise_endpoint}", json=exercise_config, headers=headers)
response.raise_for_status()
exercise_data = response.json()
print(exercise_data)

sheety_endpoint = "https://api.sheety.co/9357f34c310b67b0be01a56b1680e5c9/myWorkouts/workouts"


for exercise in exercise_data["exercises"]:
    sheety_config = {
        "workout": {
              "date": date,
              "time": time,
              "exercise": exercise["name"].title(),
              "duration": f"{exercise['duration_min']} min",
              "calories": exercise["nf_calories"]
          }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_config, auth=(os.environ["sheety_username"],
                                                                            os.environ["sheety_password"]))
    response.raise_for_status()

