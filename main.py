import datetime as dt
import pandas as pd
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

bday = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in bday.iterrows()}

if today_tuple in birthdays_dict:
    with (open(f"letter_templates/letter_{random.randint(1,3)}.txt") as template):
        contents = template.read()
        new_template = contents.replace("Angela", "Alan")
        new_contents = new_template.replace("[NAME]", birthdays_dict[today_tuple]["name"])

my_email = "100dopython@gmail.com"
gmail_password = "plkkkflgqyxpntxx"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=gmail_password)
connection.sendmail(
    from_addr=my_email,
    to_addrs=birthdays_dict[today_tuple]["email"],
    msg=f"Subject:Happy Birthday\n\n{new_contents}"
)
connection.close()
