from nonebot import get_driver
from nonebot.adapters.onebot.v11 import MessageSegment, Message
import os
import re
from utils.utils import httpx_get
from .config import Config
import feedparser
from os.path import dirname

driver = get_driver()
cfg = Config.parse_obj(get_driver().config)
path = dirname(__file__)
url = cfg.rss_url + "bilibili/user/dynamic/"


async def get_news_online(bili_uid: str) -> str:
    real_url = url + bili_uid
    res = await httpx_get(real_url)
    data = feedparser.parse(res)
    latest_news = data.entries[0]
    return latest_news


async def get_news_local(bili_uid: str) -> str:
    if os.path.exists(path + f"/news_data/{bili_uid}.xml"):
        with open(path + f"/news_data/{bili_uid}.xml", "r", encoding="UTF-8") as f:
            data = feedparser.parse(f.read())
            latest_news = data.entries[0]
            return latest_news
    else:
        real_url = url + bili_uid
        res = await httpx_get(real_url)
        data = feedparser.parse(res)
        latest_news = data.entries[0]
        with open(path + f"/news_data/{bili_uid}.xml", "w+", encoding="UTF-8") as f:
            f.write(res)
        return latest_news


async def new_news(bili_uid: str) -> bool:
    online = await get_news_online(bili_uid)
    local = await get_news_local(bili_uid)
    if online != local:
        real_url = url + bili_uid
        res = await httpx_get(real_url)
        with open(path + f"/news_data/{bili_uid}.xml", "w+", encoding="UTF-8") as f:
            f.write(res)
        return True
    else:
        return False


async def make_msg(bili_uid: str) -> Message:
    data = await get_news_local(bili_uid)
    raw_summary = data.summary
    summary = re.sub(r"<.*?>", "", raw_summary)
    raw_detail = str(data.summary_detail)
    try:
        imgs = re.findall(r"(https?://[^\s]+g)", raw_detail)
        message = summary + MessageSegment.image(imgs[0])
    except Exception:
        message = summary
    return message
