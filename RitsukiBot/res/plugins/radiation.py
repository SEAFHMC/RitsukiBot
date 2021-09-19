import nonebot
import jieba
import ujson
from random import choice
jieba.load_userdict('./res/docs/dict.txt')
bot = nonebot.get_bot()


async def del_str(str, str_list):
    for i in range(len(str_list)):
        if str == str_list[i]:
            del str_list[i]
            return str_list


async def radiation(question):
    try:
        seg_list = jieba.lcut(question, cut_all=True)
        if '文文' in seg_list and '新闻' not in seg_list:
            seg_list = await del_str('文文', seg_list)
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
    user_id = context['user_id']
    self_id = context['self_id']
    if message and user_id != self_id:
        await bot.send_group_msg(group_id=group_id, message=message)
