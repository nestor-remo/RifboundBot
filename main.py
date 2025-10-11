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

# with open("cards.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["number", "id", "orientation", "title", "altText"])

#     for card in cards:
#         writer.writerow([
#             card.get("number"),
#             card.get("id"),
#             card.get("orientation"),
#             card.get("title"),
#             card.get("altText"),
#         ])

with open("cards.json", "w") as file:
    json.dump(cards, file, indent=4)

with open("cards.json", "r") as file:
    cards = json.load(file)

print(cards[:3])

# print(cards)
# for card in cards[:3]:
#     print(f"{card.get('number')}: {card.get('title')} ({card.get('id')})")