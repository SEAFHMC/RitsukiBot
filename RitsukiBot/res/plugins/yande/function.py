import requests
from bs4 import BeautifulSoup
from random import choice


async def acurate_tag(tag):
    url = 'https://yande.re/post?tags='+tag
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    notice = soup.find_all(class_="status-notice")
    if len(notice) != 0:
        tag_list = notice[0].find_all('a')
        tag_text = ''
        for tag in tag_list:
            tag_text += tag.string.strip()+'\n'
        result = ['ask', '您是否在找：\n'+tag_text[:-1]]
    else:
        list = []
        for link in soup.find_all('a'):
            herf = link.get('href')
            try:
                if herf[-3:] == 'jpg':
                    list.append(herf)
            except TypeError:
                pass
        result = ['not_ask', choice(list)]
    return result
