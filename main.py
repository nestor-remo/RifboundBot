import requests
# from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv
import json

load_dotenv()

url = os.getenv("METADATA_URL")

response = requests.get(url)
data = response.json()

cards = data["items"]

with open("cards.json", "w") as file:
    json.dump(cards, file, indent=4)

with open("cards.json", "r") as file:
    cards = json.load(file)

cards_by_title = {}

for card in cards:
    title = card['title']
    new_card = {}
    for key, value in card.items():
        if key != 'title':
            new_card[key] = value

    cards_by_title[title] = new_card

with open("cards_by_title.json", "w") as file:
    json.dump(cards_by_title, file, indent=4)