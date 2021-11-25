import requests
from bs4 import BeautifulSoup as bs
from utils.requests_db import *


def get_info(ind):
    name, url = get_readmore_by_button(ind)
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    info = soup.find_all('div', class_='m-s-f3')
    all_info = dict()
    for i, val in enumerate(info):
        indx = val.text.find(':')
        all_info[val.text[0:indx]] = val.text[indx + 1:]
    return all_info, name
