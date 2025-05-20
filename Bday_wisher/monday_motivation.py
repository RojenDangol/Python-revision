import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import os

load_dotenv()

my_email = 'rojendangol1@gmail.com'
password = os.getenv('PASSWORD')

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open('quotes.txt') as data_file:
        data = data_file.readlines()
        quote = random.choice(data)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='rojendangol@gmail.com',
                            msg=f'Subject:Monday Motivation\n\n{quote}')
