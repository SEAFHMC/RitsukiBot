import ujson
import jieba
from random import choice
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand


async def radiation(question):
    seg_list = jieba.lcut(question, cut_all=True)
    with open('./res/docs/data.json', 'r', encoding='UTF-8') as f:
        ujsons = ujson.loads(f.read())
        if choice(seg_list) in ujsons.keys():
            return choice(ujsons[choice(seg_list)])


@on_command('radiation_chat', aliases=('二刺螈', '浓度', '高辐射'), only_to_me=False)
async def radiation_chat(session: CommandSession):
    question = session.get('question')
    result = await radiation(question)
    await session.send(result)


@radiation_chat.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'文文'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    return IntentCommand(90.0, 'radiation_chat', current_arg=stripped_msg or '')
