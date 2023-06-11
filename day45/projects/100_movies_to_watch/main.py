import requests
from bs4 import BeautifulSoup as bs

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
soup = bs(response.text, "html.parser")

movie_titles = [" ".join(title.text.split()[1:]) for title in soup.find_all(name="h3", class_="title")]
movie_titles.reverse()

with open("movies.txt", "w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
