from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11.message import MessageSegment, Message
from nonebot.adapters.onebot.v11.event import MessageEvent, PrivateMessageEvent
from nonebot.params import CommandArg
from httpx import AsyncClient


setu = on_command("setu", aliases={"涩图", "色图", "瑟图"})


@setu.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    pass