from nonebot import on_command, CommandSession, MessageSegment
from .function import acurate_tag
__plugin_name__ = 'yande'
__plugin_usage__ = r"""根据tag获取涩图（图源yande.re）
用法：/yande [tag]"""


@on_command('yande', only_to_me=False)
async def yande(session: CommandSession):
    tag = session.current_arg_text.strip()
    parser_list = await acurate_tag(tag)
    if parser_list[0] == 'ask':
        result = parser_list[1]
    else:
        result = MessageSegment.image(parser_list[1])
    await session.send(result)
