import datetime as dt
import smtplib
import random

MY_EMAIL = "some@thing.com"
MY_PASSWORD = "123456"
SMTP_ADDRS = "smtp.test.com"

now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP(SMTP_ADDRS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )