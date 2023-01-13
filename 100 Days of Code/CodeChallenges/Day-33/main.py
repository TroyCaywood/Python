import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 25.7617
MY_LONG = 80.1918

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# API request parameters
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# Split data into sunrise and sunset hour
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# Current hour
time_now = datetime.now().hour


# IS ISS within + or - 5 degrees latitude and longitude
def is_overhead():
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    else:
        return False


# Is it between sunset and sunrise
def is_dark():
    if sunset <= time_now <= sunrise:
        return True
    else:
        return False


# run every 60 seconds
while True:
    time.sleep(60)
    # Send email if ISS is overhead, and it's dark outside
    if is_overhead() and is_dark():
        my_email = "someemail@gmail.com"
        my_password = "secure_password"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Securely connect using TLS
            connection.starttls()

            # Login
            connection.login(user=my_email, password=my_password)

            # Send mail from my_email
            connection.sendmail(
                from_addr=my_email,
                to_addrs="recipientemail@gmail.com",
                msg=f"Subject: The ISS is overhead!\n\n"
                    f"Go outside and look up!"
            )
