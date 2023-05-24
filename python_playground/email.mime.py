import smtplib
from email.mime.text import MIMEText as mt
from email.mime.image import MIMEImage as mi
from email.mime.multipart import MIMEMultipart as mp
from config import CONNECTION, SENDER, PASSWORD, RECIPIENT

# Create message object
msg = mp()
msg["Subject"] = "subject message"
msg["From"] = SENDER
msg["TO"] = RECIPIENT

# Load file
with open("file_path") as file:
    text = mt(file.read())
    msg.attach(text)

# Load Image
with open("file_path", "rb") as file:
    image = mi(file.read())
    msg.attach(image)

with smtplib.SMTP(CONNECTION) as connection:
    connection.starttls()
    connection.login(user=SENDER, password=PASSWORD)
    connection.send_message(msg.as_string())
    