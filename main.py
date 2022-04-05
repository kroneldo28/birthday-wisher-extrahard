##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import os
import smtplib
import pandas


PLACEHOLDER = "[NAME]"
MY_EMAIL = "ronel.dev@yahoo.com"
with open("password.txt") as password:
    MY_PASSWORD = password.read()

SUBJECT_EMAIL = "Subject:Happy Birthday\n\n"

# 1. Update the birthdays.csv
# DONE

# 2. Check if today matches a birthday in the birthdays.csv

# We retrieve today's month and day
now = dt.datetime.now()
this_month = now.month
this_day = now.day

# We read birthday.csv
birthday_data = pandas.read_csv("birthdays.csv")
# print(birthday_data)
for (index, row) in birthday_data.iterrows():
    if row.month == this_month and row.day == this_day:
        letter = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{letter}") as letter_file:
            text = letter_file.read()
            new_text = text.replace(PLACEHOLDER, row["name"])

        # We send the quote in an email
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row.email, msg=SUBJECT_EMAIL + new_text)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
# DONE

# 4. Send the letter generated in step 3 to that person's email address.
# DONE



