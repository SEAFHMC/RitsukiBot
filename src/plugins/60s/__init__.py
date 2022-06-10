from nonebot import on_command, get_bot, get_driver
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.exception import FinishedException
from .data_source import get_60s
from .config import Config
from nonebot_plugin_apscheduler import scheduler
from asyncio import sleep as aiosleep


sixty = on_command("60s")


@sixty.handle()
async def _():
    img_url = get_60s()
    sixty.finish(MessageSegment.image(img_url))


plugin_config = Config.parse_obj(get_driver().config)
groups = plugin_config.sixty_subscribe_group


@scheduler.scheduled_job("cron", hour="7")
async def _():
    img_url = get_60s()
    bot = get_bot()
    for group in groups:
        bot.send_group_msg(group_id=group, message=MessageSegment.image(img_url))
        aiosleep(2)
        raise FinishedException
