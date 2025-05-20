import smtplib
from datetime import datetime
import random
import pandas
from dotenv import load_dotenv
import os

load_dotenv()

my_email = 'rojendangol1@gmail.com'
password = os.getenv('PASSWORD')

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt', 'r') as letter:
        content = letter.read()
        content = content.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f'Subject: Happy Birthday\n\n{content}')


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



