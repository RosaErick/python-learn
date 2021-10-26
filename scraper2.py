from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen( 'https://search.scielo.org/?lang=pt&count=15&from=0&output=site&sort=&format=summary&fb=&page=1&q=historia+do+tempo+presente')
bs = BeautifulSoup(html, 'html.parser')
