import ujson
import feedparser
from random import randint


async def get_rank(key_word):
    url = 'https://rakuen.thec.me/PixivRss/'+key_word+'-10'
    parser = feedparser.parse(url)
    ujsons = ujson.dumps(parser.entries[randint(0, 9)], indent=2, ensure_ascii=False)
    return ujson.loads(ujsons)['summary']


async def get_img_url(str):
    for i in range(len(str)):
        if str[i:i+9] == 'img src="':
            strip_start_str = str[i+9:]
            break
    for i in range(len(strip_start_str)):
        if strip_start_str[i] == '"':
            return strip_start_str[:i].strip()
            break
