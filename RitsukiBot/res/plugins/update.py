from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import os
__plugin_name__ = 'update'
__plugin_usage__ = r"""更新指定的应用(仅Admin可用)
用法：/update [app_name]
目前支持的应用有：
-cqps(cq-picsearcher-bot)
-gshpr(genshinhelper)"""


@on_command('update', permission=SUPERUSER, only_to_me=False)
async def update(session: CommandSession):
    app = session.get('app',  prompt='请输入需要更新的app：')
    if app == 'cqps':
        os.system(r'cd /root/cq-picsearcher-bot && git pull && npm i && npm restart')
        await session.send(app+'更新成功')
    elif app == 'gshpr':
        os.system(r'cd /root/genshinhelper && git pull && python setup.py install')
        await session.send(app+'更新成功')
    else:
        await session.send('不支持的应用')


@update.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['app'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('请输入有效的app名称')
    session.state[session.current_key] = stripped_arg
