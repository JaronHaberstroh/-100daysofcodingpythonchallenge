import smtplib
from config import CONNECTION, SENDER_EMAIL, PASSWORD, RECIPIENT_EMAIL

with smtplib.SMTP(CONNECTION) as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=SENDER_EMAIL,
        to_addrs=RECIPIENT_EMAIL,
        msg="Subject: Hello, this is the subject line\n\nThis is the body of the message"
        )
