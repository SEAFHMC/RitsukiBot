from nonebot.adapters.onebot.v11 import GroupMessageEvent
from .config import plugin_config


async def enable_group(event: GroupMessageEvent):
    return event.group_id in plugin_config.wordcloud_enable_group
