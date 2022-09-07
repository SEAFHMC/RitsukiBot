from nonebot.log import logger
from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.exception import FinishedException
from nonebot.params import RegexGroup
from .get_setu import Setu
from .anti_river_crab import enhanced_setu
from asyncio import sleep as asleep


setu = on_regex(r"来([0123456789]*)[份张]([rR]18)?(.*)的?[涩色瑟]图")


@setu.handle()
async def _(args=RegexGroup()):
    number = int(args[0]) if args[0].isdigit() else 1
    tag = args[2] or '"'
    if number > 10:
        await setu.finish("最多10张哦")
    resp = await Setu.get_setu(tag=tag, r18=0, number=number)
    if resp.code == 200:
        for i in resp.data:  # type: ignore
            try:
                img = await enhanced_setu(url=i.img_url, pid=i.pid)  # type: ignore
                await setu.send(MessageSegment.image(img))
                await asleep(2)
            except Exception as e:
                logger.warning(f"{type(e)}: {str(e)}")
                continue
        raise FinishedException
    await setu.finish(f"没有{tag}的涩图！")
