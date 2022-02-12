import requests
import ujson as json
from nonebot.adapters.onebot.v11 import MessageSegment
from datetime import datetime


class epicgames():
    def __init__(self, game):
        self.title = game['title']
        self.description = game['description']
        self.img = game['keyImages'][0]['url']
        self.info = game['promotions']['promotionalOffers']


async def get_epic_games():
    try:
        url = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN'
        jsons = requests.get(url).text
        jsons = json.loads(jsons)
        game_list = jsons['data']['Catalog']['searchStore']['elements']
        game_list = list(filter(lambda x: x['promotions'], game_list))
        return game_list
    except Exception:
        pass


async def get_epic_free():
    game_list = await get_epic_games()
    present = epicgames(game_list[0])
#    next = epicgames(game_list[1])
    present_endDate = present.info[0]['promotionalOffers'][0]['endDate'][:-1]
    msg = '即刻在Epic商城领取：' + present.title + '\n' +\
        MessageSegment.image(present.img) + '\n' +\
        present.description + '\n' +\
        '截止时间：' + datetime.fromisoformat(present_endDate).strftime("%Y.%m.%d %H:%M")
    if epicgames(game_list[1]):
        msg += f'\n下周可白嫖：{epicgames(game_list[1]).title}'
    return msg
