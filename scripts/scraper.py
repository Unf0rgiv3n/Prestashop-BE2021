import requests
import datetime
import csv
import os


def get_price_for_film(film_json):
    for tag in film_json["PromoLabels"]["names"]:
        if tag["name"] == "SUPERHIT":
            return 19.90
    return 16.90


def get_netto_price(price):
    return price / 1.23


file_path_film = "../assets/multikino.csv"
file_path_category = "../assets/multikino_category.csv"
rows = []
rows_category = []

rows_category.append(["Repertuar", 1, 'Sprawdź repertuar na poszczególne dni'])

for i in range(3):

    day=(datetime.datetime.today()+ datetime.timedelta(days=i)).strftime('%d-%m-%Y')
    s = requests.Session()
    url = "https://multikino.pl/api/sitecore/WhatsOn/WhatsOnV2Alphabetic?cinemaId=4&data=" + day + "&type=teraz-gramy"

    content = s.get(url).json()

    films = content["WhatsOnAlphabeticFilms"]
    for film in films:
        price = get_price_for_film(film)
        net_price = get_netto_price(price)
        rows.append([film["Title"], str(film["Synopsis"] or ""), str(price).replace(".", ","), str(round(net_price, 2)).replace(".", ","), film["Poster"],day,1,
                     film["ReleaseDate"][:10],100])

    header = ['Name', 'Description', 'Price tax included', 'Price tax excluded', 'Image URLs','Categories','Tax rule','Product creation date','Quantity']


    header_category = ['Name', 'Active','Description','Parent Category']
    rows_category.append([day,1,"Filmy grane w dniu "+day,'Repertuar'])

with open(file_path_film, 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(header)
    writer.writerows(rows)

with open(file_path_category, 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(header_category)
    writer.writerows(rows_category)

