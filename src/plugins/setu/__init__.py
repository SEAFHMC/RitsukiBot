from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11.message import MessageSegment, Message
from nonebot.params import CommandArg
from .get_setu import Setu
from .anti_river_crab import enhanced_setu


setu = on_command("setu", aliases={"涩图", "色图", "瑟图"})


@setu.handle()
async def _(arg: Message = CommandArg()):
    if not arg:
        data = await Setu.random_setu()
        if data.code == 200:
            await setu.finish(
                MessageSegment.image(
                    await enhanced_setu(url=data.img_url, pid=data.pid)
                )
            )
        await setu.finish(data.message)
    data = await Setu.search_setu(tag=arg)
    if data.code == 200:
        await setu.finish(
            MessageSegment.image(await enhanced_setu(url=data.img_url, pid=data.pid))
        )
    await setu.finish(data.message)
