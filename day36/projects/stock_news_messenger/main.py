from datetime import datetime, timedelta
import requests
from twilio.rest import Client
from config import NEWS_PARAMS, STOCK_PARAMS, TWILIO_PARAMS

def get_rounded_stock_change(y, dby):
    if y > dby:
        change = f"TSLA:🔺 {round((abs(y - dby) / y) * 100)}"
    else:
        change = f"TSLA:🔻 {round((abs(y - dby) / y) * 100)}"
    return change

# Get current date and convert for yesterday and day before yesterday stock close.
now = datetime.now()
rounded_time = now.replace(minute=0, second=0, microsecond=0, hour=19)  # ) + timedelta(hours=now.minute//30)
y_time = rounded_time - timedelta(days=1)
dby_time = y_time - timedelta(days=1)

# Make api call for stock info
stock_api_add = "https://www.alphavantage.co/query"
response = requests.get(stock_api_add, params=STOCK_PARAMS)
response.raise_for_status()
stock_data = response.json()

# find yesterday stock close and day before yesterday stock close change percentage
y_stock = float(stock_data["Time Series (60min)"][str(y_time)]["4. close"])
dby_stock = float(stock_data["Time Series (60min)"][str(dby_time)]["4. close"])
stock_percent = get_rounded_stock_change(y=y_stock, dby=dby_stock)

# Make api call for relevant news
news_api_add = "https://newsapi.org/v2/everything"
response = requests.get(news_api_add, params=NEWS_PARAMS)
response.raise_for_status()
news_data = response.json()

# Store last 3 articles in list
articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in news_data['articles'][:3]]

# Send articles and stock change via sms to phone.
account_sid = TWILIO_PARAMS["sid"]
auth_token = TWILIO_PARAMS["token"]
client = Client(account_sid, auth_token)

for article in articles:
    message = client.messages \
                    .create(
                        body=f"{stock_percent}\n {article}",
                        from_=TWILIO_PARAMS["from"],
                        to=TWILIO_PARAMS["to"]
                    )
