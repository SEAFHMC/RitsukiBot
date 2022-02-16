from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters import Bot, Event, Message
from nonebot.params import CommandArg
from nonebot import on_command
import ujson as json
from utils.utils import httpx_request
from random import choice

__plugin_name__ = 'yande'
__plugin_usage__ = r"""返回一张yande.re的涩图
用法：/yande [tag]"""

yande = on_command("yande", priority=10)


@yande.handle()
async def handle_first_receive(bot: Bot, event: Event, args: Message = CommandArg()):
    url = 'https://yande.re/post.json?tags='+args
    img_list = json.loads(await httpx_request(url))
    img_url = choice(img_list)['file_url']
    yande.finish(MessageSegment.image(img_url))
