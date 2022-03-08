from nonebot import on_command, get_driver, require
import nonebot
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent
from nonebot.typing import T_State
from nonebot.params import State, CommandArg
from .data_resource import path, new_news, make_msg
import os
import ujson as json
from nonebot.log import logger
import asyncio

driver = get_driver()


@driver.on_startup
async def _():
    if not os.path.exists(path+'/news_data'):
        os.mkdir(path+'/news_data')
    if not os.path.exists(path+'/subscribe_data.json'):
        with open(path+'/subscribe_data.json', 'w', encoding='UTF-8') as f:
            f.write(json.dumps({}))


bilisub = on_command('bilisub', priority=5, aliases={'B站订阅', 'b站订阅'})


@bilisub.handle()
async def first_receive_sub(bot: Bot, event: Event, state: T_State = State(), bili_uid=CommandArg()):
    if bili_uid := bili_uid.extract_plain_text():
        state['bili_uid'] = bili_uid


@bilisub.got("bili_uid", prompt='请输入要订阅up主的uid')
async def handle_bilisub(bot: Bot, event: Event, state: T_State = State()):
    bili_uid = state['bili_uid']
    if isinstance(event, GroupMessageEvent):
        occasion = 'groups'
        id = event.group_id
    else:
        occasion = 'users'
        id = event.user_id
    subscribe_data = path+'/subscribe_data.json'
    with open(subscribe_data, 'r', encoding='UTF-8') as f:
        data = json.loads(f.read())
    with open(subscribe_data, 'w', encoding='UTF-8') as f:
        if bili_uid not in data.keys():
            data[bili_uid] = {'groups': [], 'users': []}
            data[bili_uid][occasion] = list(set(data[bili_uid][occasion]).union([id]))
            f.write(json.dumps(data))
        else:
            data[bili_uid][occasion] = list(set(data[bili_uid][occasion]).union([id]))
            f.write(json.dumps(data))
    await bilisub.finish('订阅成功')


biliunsub = on_command('biliunsub', priority=5, aliases={'取消B站订阅', '取消b站订阅'})


@biliunsub.handle()
async def first_receive_unsub(bot: Bot, event: Event, state: T_State = State(), bili_uid=CommandArg()):
    if bili_uid := bili_uid.extract_plain_text():
        state['bili_uid'] = bili_uid


@biliunsub.got("bili_uid", prompt='请输入要取消订阅up主的uid')
async def handle_biliunsub(bot: Bot, event: Event, state: T_State = State()):
    bili_uid = state['bili_uid']
    if isinstance(event, GroupMessageEvent):
        occasion = 'groups'
        id = event.group_id
    else:
        occasion = 'users'
        id = event.user_id
    subscribe_data = path+'/subscribe_data.json'
    with open(subscribe_data, 'r', encoding='UTF-8') as f:
        data = json.loads(f.read())
    with open(subscribe_data, 'w', encoding='UTF-8') as f:
        try:
            data[bili_uid][occasion].remove(id)
        except Exception as e:
            f.write(json.dumps(data))
            await biliunsub.finish(f'取消订阅失败, {e}')
        f.write(json.dumps(data))
    await bilisub.finish('取消订阅成功')

# 每一个小时检查一次更新
scheduler = require("nonebot_plugin_apscheduler").scheduler


@scheduler.scheduled_job("cron", minute="*/30", id="Every_Half_Hour")
async def check_update():
    logger.info('chekcing BiliDynmic update')
    with open(path+'/subscribe_data.json', 'r', encoding='UTF-8') as f:
        jsons = json.loads(f.read())
    with open(path+'/subscribe_data.json', 'r', encoding='UTF-8') as f:
        data = json.loads(f.read())
    check_list = jsons.keys()
    for bili_uid in check_list:
        if await new_news(bili_uid):
            logger.info('BiliDynamic has new news')
            message = await make_msg(bili_uid)
            groups = data[bili_uid]['groups']
            users = data[bili_uid]['users']
            bot = nonebot.get_bot()
            for group_id in groups:
                await bot.send_group_msg(group_id=group_id, message=message)
                await asyncio.sleep(2)
            for user_id in users:
                await bot.send_private_msg(user_id=user_id, message=message)
                await asyncio.sleep(2)
