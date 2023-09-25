import requests
import datetime as dt
import time

MY_LAT = 32.721154
MY_LONG = -79.923285
MARGIN = 5

def check_sunset(): 
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = dt.datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        print("It's dark out!")
        return True
    else: 
        print("It's still sunny out!")
check_sunset()

def find_iss():
    global MARGIN, MY_LAT, MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT - MARGIN <= iss_latitude <= MY_LAT + MARGIN and MY_LONG - MARGIN <= iss_longitude <= MY_LONG + MARGIN:
        print("the iss is nearby!")
        return True

while True:
    time.sleep(60)
    if find_iss() and check_sunset():
        print("sending email!")
        

        









# If the ISS is close to my current position and it is currently dark, send me an email to look up. 
# BONUS: run the code every 60 seconds
