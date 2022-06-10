import asyncio
import nonebot
from nonebot import get_driver
from .config import Config

cfg = Config.parse_obj(get_driver().config)


async def msg_recall(message_id: int) -> None:
    setu_recall_time = cfg.setu_recall_time
    bot = nonebot.get_bot()
    await asyncio.sleep(setu_recall_time)
    await bot.delete_msg(message_id=message_id)
