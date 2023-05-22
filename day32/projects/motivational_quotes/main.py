import smtplib
import datetime as dt
from config import CONNECTION, SENDER_EMAIL, PASSWORD, RECIPIENT_EMAIL
from random import choice


with open("projects/motivational_quotes/quotes.txt", "r") as file:
    f_list = file.readlines()
    quote = choice(f_list)

today = dt.datetime.now()
dow = today.weekday()

if dow == 1:
    with smtplib.SMTP(CONNECTION) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject:Monday motivational quotes\n\n{quote}"
        )
