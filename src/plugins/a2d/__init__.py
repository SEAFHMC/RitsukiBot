from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from typing import List
from nonebot.params import State
from nonebot import on_command
from utils.utils import get_message_img
from .data_resource import a2d_func

__plugin_name__ = 'a2d'
__plugin_usage__ = r"""ascii2d搜图
用法：/a2d [image]"""

a2d = on_command("a2d", priority=5)


@a2d.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State = State()):
    imgs: List = get_message_img(event.json())
    if not imgs:
        await a2d.reject('图来')
    else:
        state["imgs"] = imgs


@a2d.got("imgs", prompt='图来')
async def handle_epic(bot: Bot, event: Event, state: T_State = State()):
    imgs = state['imgs']
    search_result = await a2d_func(imgs)
    result_color = (
        "色合搜索结果: " + '\n' +
        'title: ' + search_result[0]['title'] + '\n' +
        'author: ' + search_result[0]['authors'] + '\n' +
        MessageSegment.image(search_result[0]['thumbnail']) + '\n' +
        'url: ' + search_result[0]['url'])
    await a2d.send(result_color)

    result_bovm = (
        "特徽搜索结果: " + '\n' +
        'title: ' + search_result[1]['title'] + '\n' +
        'author: ' + search_result[1]['authors'] + '\n' +
        MessageSegment.image(search_result[1]['thumbnail']) + '\n' +
        'url: ' + search_result[1]['url'])
    await a2d.finish(result_bovm)
