from nonebot import require, get_bot
from nonebot.plugin import on_command, on_regex
from nonebot.adapters.onebot.v11.event import MessageEvent, GroupMessageEvent
from asyncio import sleep as asleep
from .data_source import make_msg
from .config import Config

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler


epic = on_command("epic")
epic_subscribe = on_regex(r"订阅[Ee][Pp][Ii][Cc]")
epic_unsubscribe = on_regex(r"取消订阅[Ee][Pp][Ii][Cc]")


@epic.handle()
async def _():
    await epic.finish(await make_msg())


@epic_subscribe.handle()
async def _(event: MessageEvent):
    plugin_config = Config()
    if isinstance(event, GroupMessageEvent):
        plugin_config.add_group(group_id=event.group_id)
    else:
        plugin_config.add_user(user_id=event.user_id)
    await epic_subscribe.finish("√")


@epic_unsubscribe.handle()
async def _(event: MessageEvent):
    plugin_config = Config()
    if isinstance(event, GroupMessageEvent):
        plugin_config.remove_group(group_id=event.group_id)
    else:
        plugin_config.remove_user(user_id=event.user_id)
    await epic_subscribe.finish("√")


@scheduler.scheduled_job("cron", hour="8", day_of_week="fri", id="epic_free")
async def _():
    bot = get_bot()
    msg = await make_msg()
    plugin_config = Config().parse_config()
    for group_id in plugin_config.group:
        await bot.send_group_msg(group_id=group_id, message=msg)
        await asleep(3)
    for user_id in plugin_config.user:
        await bot.send_private_msg(user_id=user_id, message=msg)
        await asleep(3)
    return
