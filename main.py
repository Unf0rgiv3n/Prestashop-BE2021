import requests
from datetime import datetime
import csv
import os


def get_price_for_film(film_json):
    for tag in film_json["PromoLabels"]["names"]:
        if tag["name"] == "SUPERHIT":
            return 19.90
    return 16.90


file_path = "multikino.csv"
photos_path = "../assets"


s = requests.Session()
url = "https://multikino.pl/api/sitecore/WhatsOn/WhatsOnV2Alphabetic?cinemaId=4&data=" + datetime.today().strftime(
    '%d-%m-%Y') + "&type=teraz-gramy"

content = s.get(url).json()

films = content["WhatsOnAlphabeticFilms"]
rows = []
for film in films:
    rows.append([film["Title"], str(film["Synopsis"] or ""), str(get_price_for_film(film)).replace(".", ","), film["Poster"]])
    divided = film["Poster"].split("/")
    poster_name = divided[len(divided) - 1]
    poster_path = os.path.join(photos_path, poster_name)
    with open(poster_path, 'wb') as handler:
        handler.write(requests.get(film["Poster"]).content)

header = ['Name', 'Description', 'Base price', 'Image URLs']
with open(file_path, 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(header)
    writer.writerows(rows)
    print(rows)
