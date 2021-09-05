from nonebot import on_command, CommandSession, MessageSegment
import json
import requests
__plugin_name__ = 'pixiv'
__plugin_usage__ = r"""1、获取Pixiv榜单并返回图片
用法：/pixivrank [key_word]
当前支持的key_word有：
daily, weekly, monthly
可在key_word后附加_r18

2、根据pid返回图片
用法：/pixivid [pid]"""


@on_command('pixivid', only_to_me=False)
async def pixivid(session: CommandSession):
    id = session.current_arg_text.strip()
    url = "https://pixiv.cat/"+id+".png"
    result = MessageSegment.image(url)
    await session.send(result)


@on_command('pixivrank', only_to_me=False)
async def pixivrank(session: CommandSession):
    rank = session.current_arg_text
    url = "https://api.loli.st/pixiv/?mode="+rank
    r = requests.get(url=url, verify=False)
    jsons = json.loads(r.text)
    id = jsons["illust_id"]
    imgurl_rank = "https://pixiv.cat/"+id+".png"
    img_r = requests.get(imgurl_rank)
    if int(img_r.status_code) == 404:
        imgurl_rank = "https://pixiv.cat/"+id+"-1.png"
    result = MessageSegment.image(imgurl_rank)
    await session.send(result)
