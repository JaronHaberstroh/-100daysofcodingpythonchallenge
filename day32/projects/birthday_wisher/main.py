import smtplib
import datetime as dt
import glob
from random import choice
from email.mime.text import MIMEText as mt
from email.mime.image import MIMEImage as mi
from email.mime.multipart import MIMEMultipart as mp
import pandas
from config import CONNECTION, SENDER, PASSWORD, RECIPIENT

# Get birthdays info
csv_data = pandas.read_csv("projects/birthday_wisher/birthdays.csv")

# Establish todays datetime
now = dt.datetime.now()

# Choose random image
images_list = glob.glob("projects/birthday_wisher/letter_templates/images/*.jpeg")
image_path = choice(images_list)
with open(image_path, "rb") as file:
    image = file.read()
    image = mi(image)
msg = mp()
msg["Subject"] = "Happy Birthday"
msg["From"] = SENDER
msg["To"] = RECIPIENT

# Choose random birthday quote
with open("projects/birthday_wisher/letter_templates/birthday_quotes.txt") as file:
    quotes = file.readlines()
    quote = choice(quotes).encode("ascii", "ignore")
    quote = quote.decode()
    quote = quote.strip(" ")
    quote = "   " + quote
    quote = mt(quote)
    
    
# Determine if birthday is today and sends completed message via email
for (index, row) in csv_data.iterrows():
    if row.month == now.month and row.day == now.day:
        # Load tempalte message
        with open("projects/birthday_wisher/letter_templates/birthday_template.txt") as file:
            message = file.read()
            message = message.replace("[NAME]", row["name"])
            message = mt(message)
        msg.attach(message)
        msg.attach(image)
        msg.attach(quote)
        with smtplib.SMTP(CONNECTION) as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            connection.sendmail(from_addr=SENDER, to_addrs=RECIPIENT, msg=msg.as_string())
