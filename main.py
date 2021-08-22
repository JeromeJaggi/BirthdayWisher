from datetime import datetime

import pandas
import random
import smtplib

SENDER_EMAIL = "happybdayfromjj@gmail.com"
PASSWORD = "Quantenschaum0po"

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 2)}.txt"
    person = birthdays_dict[today]
    with open (file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
