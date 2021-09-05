from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import os
__plugin_name__ = 'sys'
__plugin_usage__ = r"""通过Bot操作服务器(仅Admin可用)
用法：/sys [command_line]"""


@on_command('sys', permission=SUPERUSER, only_to_me=False)
async def sys(session: CommandSession):
    command_line = session.get('command_line',  prompt='请输入指令：')
    flag = int(os.system(command_line))
    if flag == 0:
        await session.send('操作成功√')
    else:
        await session.send('操作失败×')


@sys.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['command_line'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('指令不能为空')
    session.state[session.current_key] = stripped_arg
