from nonebot import on_command, get_driver, require, get_bot
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from .data_resource import make_msg, new_promotion

groups = get_driver().config.epic_subscribe_group
users = get_driver().config.epic_subscribe_user

epic = on_command("epic", priority=6)


@epic.handle()
async def _(bot: Bot, event: MessageEvent):
    res = await make_msg()
    await epic.finish(res)

scheduler = require("nonebot_plugin_apscheduler").scheduler


# 每两个小时检查一次更新
@scheduler.scheduled_job("cron", hour="*/2")
async def check_update():
    bot = get_bot()
    if await new_promotion():
        res = await make_msg()
        for group in groups:
            await bot.send_group_msg(group_id=group, message=res)
        for user in users:
            await bot.send_private_msg(user_id=user, message=res)
