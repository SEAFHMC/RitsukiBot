from nonebot.adapters.onebot.v11 import MessageSegment, GroupMessageEvent
from nonebot.adapters import Bot, Event, Message
from nonebot.params import CommandArg
from nonebot import on_command
import ujson as json
from utils.utils import httpx_request
from random import choice
from .data_resource import msg_recall


yande = on_command("yande", priority=10)
danbooru = on_command("danbooru", priority=10)
konachan = on_command("konachan", priority=10)


@yande.handle()
async def yande_handle(bot: Bot, event: Event, args: Message = CommandArg()):
    url = 'https://yande.re/post.json?tags='+str(args).strip()
    img_list = json.loads(await httpx_request(url))
    img_url = choice(img_list)['file_url']
    if isinstance(event, GroupMessageEvent):
        res = await bot.send_group_msg(group_id=event.group_id, message=MessageSegment.image(img_url))
        await msg_recall(res['message_id'])
    else:
        await yande.finish(MessageSegment.image(img_url))


@danbooru.handle()
async def danbooru_handle(bot: Bot, event: Event, args: Message = CommandArg()):
    url = 'https://danbooru.donmai.us/posts.json?tags='+str(args).strip()
    img_list = json.loads(await httpx_request(url))
    img_url = choice(img_list)['file_url']
    if isinstance(event, GroupMessageEvent):
        res = await bot.send_group_msg(group_id=event.group_id, message=MessageSegment.image(img_url))
        await msg_recall(res['message_id'])
    else:
        await danbooru.finish(MessageSegment.image(img_url))


@konachan.handle()
async def konachan_handle(bot: Bot, event: Event, args: Message = CommandArg()):
    url = 'https://konachan.com/post.json?tags='+str(args).strip()
    img_list = json.loads(await httpx_request(url))
    img_url = choice(img_list)['file_url']
    if isinstance(event, GroupMessageEvent):
        res = await bot.send_group_msg(group_id=event.group_id, message=MessageSegment.image(img_url))
        await msg_recall(res['message_id'])
    else:
        await konachan.finish(MessageSegment.image(img_url))
