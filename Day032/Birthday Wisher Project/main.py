##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "some@thing.com"
MY_PASSWORD = "123456"
SMTP_ADDRS = "smtp.test.com"

try:
    data = pandas.read_csv('birthdays.csv')
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data_dict = {}

letters = []

def sendMail(to_addrs, message):
    try:
        with smtplib.SMTP(SMTP_ADDRS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=to_addrs, 
                msg=message
            )
    except:
        print(f"Trying message to {to_addrs} with the message:\n{message}")


for n in range(3):
    file = f"letter_templates/letter_{n+1}.txt"
    with open(file) as letter_file:
        letter = letter_file.read();
        letters.append(letter)

for item in data_dict:
    birth_date = dt.datetime(item['year'], item['month'], item['day'])

    if birth_date.month == dt.datetime.today().month and birth_date.day == dt.datetime.today().day:
        letter = "Subject: Happy Birthday!!!\n\n" + str(random.choice(letters)).replace("[NAME]", item['name'])
        sendMail(item["email"], letter)

