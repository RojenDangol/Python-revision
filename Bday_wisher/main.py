import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = 'rojendangol1@gmail.com'
password = os.getenv('PASSWORD')


with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="tiishamaharjan@gmail.com",
                        msg="Subject:Hello\n\nI am practicing smtp.")
