from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")
yc_web_page = res.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_links = [item for item in article_links if not item.startswith("from")]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

highest = max(article_upvotes)
h_index = article_upvotes.index(highest)
highest_title = article_texts[h_index]
highest_link = article_links[h_index]
print(highest, highest_title, highest_link)
