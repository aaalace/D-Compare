import requests
from bs4 import BeautifulSoup

url = 'http://www.nhgp.ru/'
r = requests.get(url)
with open('../test.html', 'w', encoding='utf-8') as output_file:
    output_file.write(r.text)