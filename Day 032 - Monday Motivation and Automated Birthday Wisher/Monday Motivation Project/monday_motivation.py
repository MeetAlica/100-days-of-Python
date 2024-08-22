from email_data import USERNAME, PASSWORD, EMAIL_TO
import datetime as dt
import smtplib
import random


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(USERNAME, EMAIL_TO, msg=f"Subject:Monday Motivation\n\n{quote}")
