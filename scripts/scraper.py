import requests
from datetime import datetime
import csv
import os


def get_price_for_film(film_json):
    for tag in film_json["PromoLabels"]["names"]:
        if tag["name"] == "SUPERHIT":
            return 19.90
    return 16.90


def get_netto_price(price):
    return price / 1.23


file_path = "../assets/multikino.csv"


s = requests.Session()
url = "https://multikino.pl/api/sitecore/WhatsOn/WhatsOnV2Alphabetic?cinemaId=4&data=" + datetime.today().strftime(
    '%d-%m-%Y') + "&type=teraz-gramy"

content = s.get(url).json()

films = content["WhatsOnAlphabeticFilms"]
rows = []
for film in films:
    price = get_price_for_film(film) 
    net_price = get_netto_price(price)
    rows.append([film["Title"], str(film["Synopsis"] or ""), str(price).replace(".", ","), str(round(net_price, 2)).replace(".", ","), film["Poster"]])

header = ['Name', 'Description', 'Price tax included', 'Price tax excluded', 'Image URLs']

with open(file_path, 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(header)
    writer.writerows(rows)

