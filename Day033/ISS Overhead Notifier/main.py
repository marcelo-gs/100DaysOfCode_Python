from tkinter.constants import TRUE
import requests
from datetime import datetime, timedelta
import time
import smtplib

_DEBUB_ = True

MY_LAT = -23.603918 # Your latitude
MY_LONG = -46.799494 # Your longitude
MY_EMAIL = "some@thing.com"
MY_PASSWORD = "123456"
SMTP_ADDRS = "smtp.test.com"

def sendMail(to_addrs, subject, message):
    send_message = f"""
    Subject: {subject}
    

    {message}
    
    _This message was send by Marcelo Gomes in a Python Program_
    """
    try:
        with smtplib.SMTP(SMTP_ADDRS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=to_addrs, 
                msg=send_message
            )
    except:
        print(f"Trying message to {to_addrs} with the message:\n{message}")


def utc2local (utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print((iss_latitude, iss_longitude))
    return (iss_latitude, iss_longitude)

def is_closer(iss_location) -> bool:
    #Your position is within +5 or -5 degrees of the ISS position.
    my_bottom_lat = MY_LAT - 5.0
    my_up_lat = MY_LAT + 5.0
    my_bottom_lng = MY_LONG- 5.0
    my_up_lng = MY_LONG + 5.0
    is_closer_lat = (my_bottom_lat >= iss_location[0] and iss_location[0] <= my_up_lat)
    is_closer_long = (my_bottom_lng >= iss_location[1] and iss_location[1] <= my_up_lng)
    if is_closer_lat and is_closer_long:
        return True
    else:
        return False
    

def is_dark() -> bool:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunset = datetime(year=int(data["results"]["sunset"].split("T")[0].split("-")[0]),  
                        month=int(data["results"]["sunset"].split("T")[0].split("-")[1]),
                        day=int(data["results"]["sunset"].split("T")[0].split("-")[2]),
                        hour=int(data["results"]["sunset"].split("T")[1].split(":")[0]),
                        minute=int(data["results"]["sunset"].split("T")[1].split(":")[1]), 
                        second=int(data["results"]["sunset"].split("T")[1].split(":")[2].split("+")[0])
    ) 
    sunrise = datetime(year=int(data["results"]["sunrise"].split("T")[0].split("-")[0]),  
                        month=int(data["results"]["sunrise"].split("T")[0].split("-")[1]),
                        day=int(data["results"]["sunrise"].split("T")[0].split("-")[2]),
                        hour=int(data["results"]["sunrise"].split("T")[1].split(":")[0]),
                        minute=int(data["results"]["sunrise"].split("T")[1].split(":")[1]), 
                        second=int(data["results"]["sunrise"].split("T")[1].split(":")[2].split("+")[0])     
    ) 

    sunset = utc2local(sunset)
    sunrise += timedelta(days=1)
    sunrise = utc2local(sunrise)
    time_now = datetime.now()
    if time_now >= sunset and time_now <= sunrise:
        return True
    else:
        return False
    

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

program_is_on = True
execution = 0

while program_is_on:

    if _DEBUB_ == True:
        ## This only to test
        execution += 1
        if execution > 5:
            program_is_on = False
    else:
        pass

    try:
        if is_closer(get_iss_location()) and is_dark():
            sendMail("me@test.com", 
            "ISS is Overheaad", 
            "Look to the Sky maybe you can see ISS on the dark of the Sky.")
        time.sleep(60)
    except:
        program_is_on = False
