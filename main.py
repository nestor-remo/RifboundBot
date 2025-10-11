import requests
# from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("METADATA_URL")

response = requests.get(url)
data = response.json()

cards = data["items"]
# print(data)

with open("cards.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["number", "id", "orientation", "title", "altText"])

    for card in cards:
        writer.writerow([
            card.get("number"),
            card.get("id"),
            card.get("orientation"),
            card.get("title"),
            card.get("altText"),
        ])

print(cards)
# for card in cards[:3]:
#     print(f"{card.get('number')}: {card.get('title')} ({card.get('id')})")