from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11.message import MessageSegment, Message
from nonebot.adapters.onebot.v11.event import MessageEvent, PrivateMessageEvent
from nonebot.params import CommandArg
from httpx import AsyncClient


setu = on_command("setu", aliases={"涩图", "色图", "瑟图"})


@setu.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    if not arg:
        await setu.finish(
            MessageSegment.image("http://127.0.0.1:61658/setu/random?r18=0")
        )
    if arg.extract_plain_text() == "r18" and isinstance(event, PrivateMessageEvent):
        await setu.finish(
            MessageSegment.image("http://127.0.0.1:61658/setu/random?r18=1")
        )
    args = arg.extract_plain_text().split()
    async with AsyncClient() as client:
        if args[0] == "r18" and isinstance(event, PrivateMessageEvent):
            resp = await client.get(
                f"http://127.0.0.1:61658/setu/search?tag={args[1]}&r18=1"
            )
        else:
            resp = await client.get(
                f"http://127.0.0.1:61658/setu/search?tag={args[0]}&r18=0"
            )
    if resp.json()["code"] == 200:
        await setu.finish(
            MessageSegment.image(
                resp.json()["img_url"].replace(
                    "https://i.pximg.net/", "http://127.0.0.1:17777/pixiv/"
                )
            )
        )
    await setu.finish(resp.json()["message"])
