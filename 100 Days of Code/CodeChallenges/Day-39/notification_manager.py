import os
from twilio.rest import Client
import smtplib


TWILIO_SID = os.environ[TWILIO_SID]
TWILIO_AUTH_TOKEN = os.environ[TWILIO_AUTH_TOKEN]
TWILIO_VIRTUAL_NUMBER = os.environ[TWILIO_VIRTUAL_NUMBER]
TWILIO_VERIFIED_NUMBER = os.environ[TWILIO_VERIFIED_NUMBER]
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "EMAIL"
MY_PASSWORD = "PASSWORD"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )