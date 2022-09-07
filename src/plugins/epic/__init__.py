from nonebot import require
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment
from asyncio import sleep as asleep
from .data_source import get_epic

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler


@scheduler.scheduled_job("cron", hour="8", week="4", id="epic_free")
async def send_msg():
    (present, next) = await get_epic()
    for game in present:
        msg = MessageSegment.text(f"即刻在Epic商城领取{game.title}")
        msg += MessageSegment.image(game.keyImages[0].url)
        msg += MessageSegment.text(game.description)
        await epic.send(msg)
        await asleep(2)
    msg = MessageSegment.text(f"下周可白嫖{'和'.join([i.title for i in next])}")
    await asleep(2)
    await epic.finish(msg)


epic = on_command("epic")
epic.handle()(send_msg)
