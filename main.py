import requests
from bs4 import BeautifulSoup


# Makes GET request
r = requests.get("https://www.twitch.tv/")

# Checks status code and success code

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())