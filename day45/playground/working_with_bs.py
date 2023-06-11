import requests
from bs4 import BeautifulSoup as bs

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = bs(yc_web_page, "html.parser")
all_articles = soup.find_all(name="a", rel="noreferrer")
article_texts = [text.text for text in all_articles]
aarticle_links = [article.get("href") for article in all_articles]
article_scores = [int(score.text.strip("points")) for score in soup.find_all(name="span", class_="score")]
# print(*article_scores, sep="\n")

highest_score = max(article_scores)
highest_score_index = article_scores.index(highest_score)
print(f"{highest_score}, {highest_score_index}")