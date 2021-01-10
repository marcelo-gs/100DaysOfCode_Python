import requests
from datetime import datetime

APP_ID  = "APP_ID"  
API_KEY = "API_KEY"
GENDER = "male"
WEIGHT_KG = "77"
HEIGHT_CM = "170"
AGE = "32"

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/<sheetID>/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID, 
    "x-app-key": API_KEY, 
    "Content-Type":"application/json"
}

exercise_text = input("Tell me which exercises you did: ")
body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=end_point, json=body, headers=headers)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
body_sheet = {
   "workout" : {
        "date" : today_date, 
        "time" : now_time, 
        "exercise": "Testing",
        "duration" : "2",
        "calories" : "100"
   }
}

headers = {
    "Content-Type":"application/json"
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
#No Authentication  
response = requests.post(url=sheet_endpoint, json=body_sheet, headers=headers)
print(response.text)

#Basic Authentication
response = requests.post(
  url=sheet_endpoint, 
  json=body_sheet, 
  headers=headers,
  auth=(
      "YOUR USERNAME", 
      "YOUR PASSWORD",
  )
)

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {'YOUR TOKEN'}"
}
response = requests.post(
  url=sheet_endpoint, 
  json=body_sheet, 
  headers=bearer_headers
  )