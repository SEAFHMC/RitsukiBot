import feedparser
import ujson


async def get_img_url(str):
    for i in range(len(str)):
        if str[i:i+9] == 'img src="':
            strip_start_str = str[i+9:]
            break
    for i in range(len(strip_start_str)):
        if strip_start_str[i] == '"':
            return strip_start_str[:i].strip()
            break


async def strip_deco(str):
    count = -1
    for i in str:
        count += 1
        if i == '<' or i == '#':
            break
    return str[:count]


async def check_update(rss_id):
    with open('./res/plugins/rss/'+rss_id.replace('/', '-')+'.json', 'r', encoding='UTF-8') as f:
        url = r'http://107.182.17.60:1200/'+rss_id
        parser = feedparser.parse(url)
        ujsons = ujson.dumps(parser.entries[0], indent=2, ensure_ascii=False)
        if ujsons == f.read():
            return False
        else:
            return True


async def get_update(rss_id):
    with open('./res/plugins/rss/'+rss_id.replace('/', '-')+'.json', 'w+', encoding='UTF-8') as f:
        url = r'http://107.182.17.60:1200/'+rss_id
        parser = feedparser.parse(url)
        ujsons = ujson.dumps(parser.entries[0], indent=2, ensure_ascii=False)
        f.write(ujsons)
        return ujson.loads(ujsons)
