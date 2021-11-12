import requests
from datetime import datetime
from threading import Thread
from queue import Queue
import csv
import os


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory, link = self.queue.get()
            try:
                download_image(link, directory)
            finally:
                self.queue.task_done()


def get_price_for_film(film_json):
    for tag in film_json["PromoLabels"]["names"]:
        if tag["name"] == "SUPERHIT":
            return 19.90
    return 16.90


def download_image(poster_url, path):
    with open(path, 'wb') as handler:
        handler.write(requests.get(poster_url).content)


file_path = "multikino.csv"
photos_path = "../`assets"


s = requests.Session()
url = "https://multikino.pl/api/sitecore/WhatsOn/WhatsOnV2Alphabetic?cinemaId=4&data=" + datetime.today().strftime(
    '%d-%m-%Y') + "&type=teraz-gramy"

content = s.get(url).json()

films = content["WhatsOnAlphabeticFilms"]
rows = []
film_urls = []
for film in films:
    divided = film["Poster"].split("/")
    poster_name = divided[len(divided) - 1]
    poster_path = os.path.join(photos_path, poster_name)
    rows.append([film["Title"], str(film["Synopsis"] or ""), str(get_price_for_film(film)).replace(".", ","), poster_path])
    film_urls.append(film["Poster"])

queue = Queue()
# Create 8 worker threads
for x in range(8):
    worker = DownloadWorker(queue)
    # Setting daemon to True will let the main thread exit even though the workers are blocking
    worker.daemon = True
    worker.start()
# Put the tasks into the queue as a tuple
for i, u in enumerate(film_urls):
    if not os.path.isfile(rows[i][3]):
        queue.put((rows[i][3], u))
# Causes the main thread to wait for the queue to finish processing all the tasks
queue.join()

header = ['Name', 'Description', 'Base price', 'Image URLs']
with open(file_path, 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(header)
    writer.writerows(rows)

