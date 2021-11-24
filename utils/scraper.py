import requests
from bs4 import BeautifulSoup as bs
url = 'https://www.e-katalog.ru/ONEPLUS-9-PRO-128GB.htm'
r = requests.get(url)
soup = bs(r.text, 'lxml')
info = soup.find_all('div', class_='m-s-f3')
all_info = dict()


def get_info():
    for i, val in enumerate(info):
        all_info[val.text.split(':')[0]] = val.text.split(':')[1]
    return all_info


def get_pic():
    return 'static/iphone_12.jpg'
