import requests
import smtplib
from bs4 import BeautifulSoup as bs
from config import SMTP

BUY_PRICE = 300
URL = "https://www.amazon.com/Bloodborne-Board-Game-Blood-Expansion/dp/B08WHWLDNM/ref=sr_1_102?crid=3TEON94EAOAYR&keywords=board+games&qid=1686894251&refinements=p_36%3A1253564011&rnid=386491011&s=toys-and-games&sprefix=board+games%2Caps%2C92&sr=1-102"
HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "upgrade-insecure-requests": "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "te": "trailers",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "132.147.59.227",
}
response = requests.get(url=URL, headers=HEADER)
soup = bs(response.text, "html.parser")
price = soup.find(class_="a-price-whole").get_text()
price_as_float = float(price)

if BUY_PRICE > price_as_float:
    with smtplib.SMTP(SMTP["connection"]) as connection:
        connection.starttls()
        connection.login(
            user=SMTP["sender"],
            password=SMTP["password"])
        connection.sendmail(
            from_addr=SMTP["sender"],
            to_addrs=SMTP["recipient"],
            msg=f"Subject:Amazon Price Check\n\nYour price has come down to {price_as_float}"
            )
