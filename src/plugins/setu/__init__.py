from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters import Bot, Event, Message
from nonebot.params import CommandArg
from nonebot import on_command
import ujson as json
from utils.utils import httpx_request
from random import choice


yande = on_command("yande", priority=10)
danbooru = on_command("danbooru", priority=10)
konachan = on_command("konachan", priority=10)


@yande.handle()
async def yande_handle(bot: Bot, event: Event, args: Message = CommandArg()):
    url = 'https://yande.re/post.json?tags='+str(args).strip()
    img_list = json.loads(await httpx_request(url))
    img_url = choice(img_list)['file_url']
    await yande.finish(MessageSegment.image(img_url))


@danbooru.handle()
async def danbooru_handle(bot: Bot, event: Event, args: Message = CommandArg()):
    url = 'https://danbooru.donmai.us/posts.json?tags='+str(args).strip()
    img_list = json.loads(await httpx_request(url))
    img_url = choice(img_list)['file_url']
    await danbooru.finish(MessageSegment.image(img_url))


@konachan.handle()
async def konachan_handle(bot: Bot, event: Event, args: Message = CommandArg()):
    url = 'https://konachan.com/post.json?tags='+str(args).strip()
    img_list = json.loads(await httpx_request(url))
    img_url = choice(img_list)['file_url']
    await konachan.finish(MessageSegment.image(img_url))
