from datetime import datetime

import requests
MY_LATS = 27.717245
MY_LONG = 85.323959

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude,latitude)
# print(iss_position)
parameters = {
    "lat": MY_LATS,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
# print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
