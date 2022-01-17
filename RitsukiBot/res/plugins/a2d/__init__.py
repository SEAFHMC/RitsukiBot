from nonebot import on_command, CommandSession, MessageSegment
from .function import a2d
__plugin_name__ = 'a2d'
__plugin_usage__ = r"""ascii2d搜图
用法：/a2d [image]"""


@on_command('a2d', only_to_me=False)
async def a2d_search(session: CommandSession):
    CQCode = session.get('CQCode', prompt='图来')
    search_result = await a2d(CQCode)
    result_color = (
        "色合搜索结果: " + '\n' +
        'title: ' + search_result[0]['title'] + '\n' +
        'author: ' + search_result[0]['authors'] + '\n' +
        MessageSegment.image(search_result[0]['thumbnail']) + '\n' +
        'url: ' + search_result[0]['url'])
    await session.send(result_color)

    result_bovm = (
        "特徽搜索结果: " + '\n' +
        'title: ' + search_result[1]['title'] + '\n' +
        'author: ' + search_result[1]['authors'] + '\n' +
        MessageSegment.image(search_result[1]['thumbnail']) + '\n' +
        'url: ' + search_result[1]['url'])
    await session.send(result_bovm)
