import requests
from bs4 import BeautifulSoup
import csv

URL = "https://search.scielo.org/?lang=pt&count=5&from=0&output=site&sort=&format=summary&fb=&page=1&q=historia+do+tempo+presente"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

last_links = soup.find(class_='modal fade')
last_links.decompose()

result_title_list = soup.find_all(class_='a')
result_title_list_items = soup.find_all(class_='title')

for result_title in result_title_list_items:
    names = result_title.contents[0]

print(names)
