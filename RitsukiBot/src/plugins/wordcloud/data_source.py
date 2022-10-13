from nonebot.adapters.onebot.v11 import GroupMessageEvent
from time import localtime, strftime
from typing import Union
from .config import plugin_config


async def enable_group(event: GroupMessageEvent):
    return event.group_id in plugin_config.wordcloud_enable_group


def format_time(timestamp: Union[int, float]):
    return strftime("%Y-%m-%d", localtime(timestamp))
