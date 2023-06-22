import requests
from bs4 import BeautifulSoup as bs


class WebScraper:
    def __init__(self, date) -> None:
        self.date = date
        self.url = "https://www.billboard.com/charts/hot-100"

    def get_songs(self):
        response = requests.get(f"{self.url}/{self.date}")
        soup = bs(response.text, "html.parser")
        song_data = soup.select("li ul li h3")
        song_titles = [song.text.strip() for song in song_data]
        return song_titles
