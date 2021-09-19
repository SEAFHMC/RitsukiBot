import nonebot
import jieba
import ujson
from random import choice
bot = nonebot.get_bot()


async def radiation(question):
    try:
        seg_list = jieba.lcut(question, cut_all=True)
        if seg_list[0] == '文文' and '新闻' not in seg_list:
            del seg_list[0]
            with open('./res/docs/data.json', 'r', encoding='UTF-8') as f:
                ujsons = ujson.loads(f.read())
                init = []
                for i in seg_list:
                    if i in ujsons.keys():
                        init.append(i)
                init = choice(init)
                if init in ujsons.keys():
                    return choice(ujsons[init])
        else:
            pass
    except:
        pass


@bot.on_message('group')
async def chat(context):
    message = context['raw_message'].strip()
    group_id = context['group_id']
    message = await radiation(message)
    if message:
        await bot.send_group_msg(group_id=group_id, message=message)
