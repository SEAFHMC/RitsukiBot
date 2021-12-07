import requests
from bs4 import BeautifulSoup
from random import choice


async def acurate_tag(tag):
    url = 'https://yande.re/post?tags='+tag
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    list = []
    for link in soup.find_all('a'):
        herf = link.get('href')
        try:
            if herf[-3:] == 'jpg':
                list.append(herf)
        except TypeError:
            pass
    return choice(list)
