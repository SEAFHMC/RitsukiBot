from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.params import RegexGroup
from .get_setu import Setu
from .anti_river_crab import enhanced_setu


setu = on_regex(r"来([0123456789]*)[份张]([rR]18)?(.*)的?[涩色瑟]图")


@setu.handle()
async def _(event: MessageEvent, args=RegexGroup()):
    number = int(args[0]) if args[0].isdigit() else 1
    tag = args[2] or '"'
    if number > 10:
        await setu.finish("最多10张哦")
    resp = await Setu.get_setu(tag=tag, r18=0, number=number)
    if resp.code == 200:
        msg = MessageSegment.reply(event.message_id)
        for i in resp.data:
            msg += MessageSegment.image(await enhanced_setu(url=i.img_url, pid=i.pid))
        await setu.finish(msg)
    await setu.finish(resp.message)
