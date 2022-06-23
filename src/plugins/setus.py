from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11.message import MessageSegment, Message
from nonebot.params import CommandArg
from httpx import AsyncClient


setu = on_command("setu", aliases={"涩图", "色图", "瑟图"})


@setu.handle()
async def _(arg:Message=CommandArg()):
    if not arg:
        await setu.finish(MessageSegment.image("http://127.0.0.1:61658/setu/random"))
    async with AsyncClient() as client:
        resp = await client.get(f"http://127.0.0.1:61658/setu/search?tag={arg.extract_plain_text()}")
    if resp.json()["code"] == 200:
        await setu.finish(MessageSegment.image(resp.json()["img_url"]))
    await setu.finish(resp.json()["message"])
