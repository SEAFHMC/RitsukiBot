from nonebot import on_command, get_bot, get_driver, require
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.exception import FinishedException
from .data_source import get_60s
from .config import Config
from asyncio import sleep as aiosleep


sixty = on_command("60s")


@sixty.handle()
async def _():
    img_url = await get_60s()
    await sixty.finish(MessageSegment.image(img_url))


plugin_config = Config.parse_obj(get_driver().config)
groups = plugin_config.sixty_subscribe_group

scheduler = require("nonebot_plugin_apscheduler").scheduler


@scheduler.scheduled_job("cron", hour="8")
async def _():
    img_url = await get_60s()
    bot = get_bot()
    for group in groups:
        await bot.send_group_msg(group_id=group, message=MessageSegment.image(img_url))
        await aiosleep(2)
        raise FinishedException
