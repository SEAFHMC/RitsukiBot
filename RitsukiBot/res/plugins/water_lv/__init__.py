from nonebot import on_command, CommandSession
from .function import get_dc_lv, get_xc_lv
__plugin_name__ = '水位'
__plugin_usage__ = r"""生成每日水位监测报告
用法：/水位 [当前测量水位]"""


@on_command('dcsw')
async def dc_lv(session: CommandSession):
    shuiwei = session.get('shuiwei', prompt='请输入目前水位：')
    shuiwei_result = await get_dc_lv(shuiwei)
    await session.send(shuiwei_result)


@dc_lv.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['shuiwei'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('水位不能为空，请重新输入')
    session.state[session.current_key] = stripped_arg


@on_command('xcsw')
async def xc_lv(session: CommandSession):
    shuiwei = session.get('shuiwei', prompt='请输入目前水位：')
    shuiwei_result = await get_xc_lv(shuiwei)
    await session.send(shuiwei_result)


@xc_lv.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['shuiwei'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('水位不能为空，请重新输入')
    session.state[session.current_key] = stripped_arg
