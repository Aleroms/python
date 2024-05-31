import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_valid_date():
    while True:
        user_input = input("Enter a date (YYYY-MM-DD format): ")
        try:
            # Try parsing the input date in YYYY-MM-DD format
            date = datetime.strptime(user_input, "%Y-%m-%d")
            return date.strftime("%Y-%m-%d")  # Return date in the desired format
        except ValueError:
            try:
                # Try parsing the input date in other possible formats
                date = datetime.strptime(user_input, "%m/%d/%Y")
                return date.strftime("%Y-%m-%d")  # Return date in the desired format
            except ValueError:
                try:
                    # Try parsing the input date in another possible format
                    date = datetime.strptime(user_input, "%d-%m-%Y")
                    return date.strftime("%Y-%m-%d")  # Return date in the desired format
                except ValueError:
                    print("Invalid date format. Please enter a valid date.")


# Example usage
# date = get_valid_date()

url = "https://www.billboard.com/charts/hot-100/1997-09-17"
res = requests.get(url=url)
res.raise_for_status()
billboard_page = res.text
soup = BeautifulSoup(billboard_page, "html.parser")
# ranks = soup.select(selector=".c-label")


song_artist_span = soup.select(selector="div ul li ul li span")
song_artists = [song.getText().strip() for song in song_artist_span]
song_name_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_span]

print(song_artists, song_names)