from nonebot import on_message, get_driver
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from nonebot.rule import to_me
from nonebot.params import EventMessage
import ujson as json
from random import shuffle, choice
from os.path import dirname

path = dirname(__file__)
driver = get_driver()


@driver.on_startup
async def GetJson():
    with open(path + "/data.json", "r", encoding="UTF-8") as f:
        global data
        data = json.loads(f.read())


radiation = on_message(rule=to_me(), priority=99)


@radiation.handle()
async def _(bot: Bot, event: Event, msg: Message = EventMessage()):
    keys = list(data.keys())
    shuffle(keys)
    for i in keys:
        if i in msg.extract_plain_text():
            await radiation.finish(choice(data[i]))
