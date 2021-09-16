from nonebot import on_command, CommandSession, MessageSegment
from .function import get_rank, get_img_url
__plugin_name__ = 'pixiv'
__plugin_usage__ = r"""1、获取Pixiv榜单并返回图片
用法：/pixivrank [key_word]
当前支持的key_word有：
daily, weekly, monthly,
rookie,original,male,female
可在key_word后附加_r18

2、根据pid返回图片
用法：/pixivid [pid]"""


@on_command('pixivid', only_to_me=False)
async def pixivid(session: CommandSession):
    id = session.current_arg_text.strip()
    url = "https://pixiv.cat/"+id+".png"
    result = MessageSegment.image(url)
    await session.send(result)


@on_command('pixivrank', only_to_me=False)
async def pixivrank(session: CommandSession):
    rank = session.current_arg_text.strip()
    rank_summary = await get_rank(rank)
    imgurl_rank = await get_img_url(rank_summary)
    result = MessageSegment.image(imgurl_rank)
    await session.send(result)
