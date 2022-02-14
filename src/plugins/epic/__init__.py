from nonebot import on_command, get_driver, require, get_bot, logger
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from .data_resource import make_msg, new_promotion, path, url
import os
from utils.utils import httpx_request

driver = get_driver()
groups = get_driver().config.epic_subscribe_group
users = get_driver().config.epic_subscribe_user

epic = on_command("epic", priority=6)


@driver.on_startup
async def first_run():
    if not os.path.exists(path+"/epic.json"):
        logger.info('正在创建epic.json')
        content = await httpx_request(url)
        with open(path+'/epic.json', 'w+', encoding='UTF-8') as f:
            f.write(content)


@epic.handle()
async def _(bot: Bot, event: MessageEvent):
    res = await make_msg()
    await epic.finish(res)

scheduler = require("nonebot_plugin_apscheduler").scheduler


# 每两个小时检查一次更新
@scheduler.scheduled_job("cron", hour="*/2", id="Every_TwoHours")
async def check_update():
    if await new_promotion():
        bot = get_bot()
        res = await make_msg()
        for group in groups:
            await bot.send_group_msg(group_id=group, message=res)
        for user in users:
            await bot.send_private_msg(user_id=user, message=res)
