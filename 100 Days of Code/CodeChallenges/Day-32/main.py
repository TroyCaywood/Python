##################### Normal Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas

# Get current date/time and assign month and day variables. Create tuple for dictionary.
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

# Read CSV and create dictionary using month and day as key
data = pandas.read_csv("birthdays.csv")
print(data)
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# If today's date is in birthday's dict send letter
if (today_month, today_day) in birthdays_dict:

    # Get name for current day
    name = birthdays_dict[(today_month, today_day)]["name"]
    letter_number = random.randint(1, 3)
    letter = f"./letter_templates/letter_{letter_number}.txt"

    # Read letter and replace name
    with open(file=letter) as picked_letter:
        read_letter = picked_letter.read()
        final_letter = read_letter.replace("[NAME]", name.rstrip("\r\n"))

    # Send email
    my_email = "someemail@gmail.com"
    password = "somepassword"
    to_address = birthdays_dict[(today_month, today_day)]["email"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # Send letter with replaced name
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"Subject: It's your birthday!\n\n{final_letter}")



