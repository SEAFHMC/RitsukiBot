from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.adapters.onebot.v11.event import GroupMessageEvent, MessageEvent
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.exception import FinishedException
from nonebot.params import RegexGroup
from .get_setu import Setu
from .anti_river_crab import enhanced_setu


setu = on_regex(r"来([0123456789]*)[份张]([rR]18)?(.*)的?[涩色瑟]图")


@setu.handle()
async def _(bot: Bot, event: MessageEvent, args=RegexGroup()):
    number = int(args[0]) if args[0].isdigit() else 1
    tag = args[2] or '"'
    if number > 10:
        await setu.finish("最多10张哦")
    resp = await Setu.get_setu(tag=tag, r18=0, number=number)
    if resp.code == 200:
        msg = []
        try:
            for i in resp.data:
                msg.append(
                    MessageSegment(
                        "node",
                        {
                            "uin": bot.self_id,
                            "name": "Bot",
                            "content": MessageSegment.image(
                                await enhanced_setu(url=i.img_url, pid=i.pid)
                            ),
                        },
                    )
                )
        except Exception:
            pass
        if isinstance(event, GroupMessageEvent):
            await bot.send_group_forward_msg(group_id=event.group_id, messages=msg)
        else:
            await bot.send_private_forward_msg(user_id=event.user_id, messages=msg)
        raise FinishedException
    await setu.finish(resp.message)
