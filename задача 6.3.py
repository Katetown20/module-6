import requests
from datetime import datetime
from threading import Thread

def get_html(link):
    r = requests.get('https://www.kinopoisk.ru/')
    print(r.text)
    print(f'thread name {link}')

for i in range(5):
    get_html(i+1)

t1 = datetime.now()

print('time', (datetime.now() - t1).microseconds)
threads = [Thread(target= get_html, args= (i +1,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print('time', (datetime.now() - t1).microseconds)