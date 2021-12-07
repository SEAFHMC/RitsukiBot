from nonebot import on_command, CommandSession, MessageSegment
from .function import acurate_tag
__plugin_name__ = 'yande'
__plugin_usage__ = r"""根据tag获取涩图（图源yande.re）
用法：/yande [tag]"""


@on_command('yande', only_to_me=False)
async def yande(session: CommandSession):
    tag = session.current_arg_text.strip()
    url = await acurate_tag(tag)
    result = MessageSegment.image(url)
    await session.send(result)
