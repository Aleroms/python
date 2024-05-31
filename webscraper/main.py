import requests
from bs4 import BeautifulSoup

# get website data
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
res = requests.get(url=url).text

soup = BeautifulSoup(res, "html.parser")
movie_tag = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movie_tag]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        try:
            file.write(f"{movie}\n")
        except:
            continue
