import ujson as json
from nonebot import logger
from nonebot.adapters.onebot.v11 import MessageSegment
from datetime import datetime
from os.path import dirname
from utils.utils import httpx_get
from typing import List

# 首次运行，创建目录和文件
url = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN'
path = dirname(__file__)


class epicgames():
    def __init__(self, game):
        self.title = game['title']
        self.description = game['description']
        self.img = game['keyImages'][0]['url']
        self.info = game['promotions']['promotionalOffers']


async def get_game_list_online() -> List:
    try:
        jsons = await httpx_get(url)
        jsons = json.loads(jsons)
        game_list = jsons['data']['Catalog']['searchStore']['elements']
        game_list = list(filter(lambda x: x['promotions'], game_list))
        present = epicgames(list(filter(lambda x: x['promotions']['promotionalOffers'], game_list))[0])
        next = epicgames(list(filter(lambda x: x['promotions']['upcomingPromotionalOffers'], game_list))[0])
        game_list = [present, next]
        return game_list
    except Exception as e:
        logger.error('Error occured'+e)
        return []


async def get_game_list_local() -> List:
    try:
        with open(path+'/epic.json', 'r', encoding='UTF-8') as f:
            jsons = f.read()
        jsons = json.loads(jsons)
        game_list = jsons['data']['Catalog']['searchStore']['elements']
        game_list = list(filter(lambda x: x['promotions'], game_list))
        present = epicgames(list(filter(lambda x: x['promotions']['promotionalOffers'], game_list))[0])
        next = epicgames(list(filter(lambda x: x['promotions']['upcomingPromotionalOffers'], game_list))[0])
        game_list = [present, next]
        return game_list
    except Exception as e:
        logger.error('Error occured'+e)
        return []


async def new_promotion():
    local = await get_game_list_local()
    online = await get_game_list_online()
    if local[0].title != online[0].title:
        logger.info('Epic白嫖发现更新')
        with open(path+'/epic.json', 'w', encoding='UTF-8') as f:
            jsons = await httpx_get(url)
            f.write(jsons)
        return True
    else:
        return False


async def make_msg():
    game_list = await get_game_list_local()
    present = game_list[0]
    next = game_list[1]
    present_endDate = present.info[0]['promotionalOffers'][0]['endDate'][:-1]
    msg = '即刻在Epic商城领取：' + present.title + '\n' +\
        MessageSegment.image(present.img) + '\n' +\
        present.description + '\n' +\
        '截止时间：' + datetime.fromisoformat(present_endDate).strftime("%Y.%m.%d %H:%M")
    if next:
        msg += f'\n下次可白嫖：{next.title}'
    return msg
