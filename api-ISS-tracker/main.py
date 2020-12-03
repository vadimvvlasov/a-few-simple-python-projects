import requests
from datetime import datetime
import smtplib
import time

def get_distance(a, b):
    """return distance between `a` and `b`"""
    return sum([(b[i] - a[i]) ** 2 for i in range(len(a))]) ** .5

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: ISS in the sky\n\nHey, look UP!!!!\nISS is above you in the sky"
        )


MY_EMAIL = "popkinpetya1@gmail.com"
MY_PASSWORD = "spectr222"


MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

def is_iss_overjead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    iss_overjead = get_distance((MY_LAT, MY_LONG), (iss_latitude, iss_longitude)) < 5
    print(iss_overjead)
    return iss_overjead,get_distance((MY_LAT, MY_LONG), (iss_latitude, iss_longitude))


def is_night():
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

    time_now = datetime.now().hour
    return time_now <= sunrise or time_now >= sunset

# If the ISS is close to my current position


# and it is currently dark

# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    print(datetime.now(),f", distance={is_iss_overjead()[1]},", is_night() and is_iss_overjead()[0])

    if is_night() and is_iss_overjead()[0]:
        send_email()
# BONUS: run the code every 60 seconds.
