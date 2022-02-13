import ujson
from typing import List
from nonebot.adapters.onebot.v11 import MessageSegment


def get_message_img(data: str) -> List[str]:
    """
    说明：
        获取消息中所有的 图片 的链接
    参数：
        :param data: event.json()
    """
    try:
        img_list = []
        data = ujson.loads(data)
        for msg in data["message"]:
            if msg["type"] == "image":
                img_list.append(msg["data"]["url"])
        return img_list
    except KeyError:
        return []


def make_node(msg):
    node = {
        'type': 'node',
        'data': {
            'uin': 2854196306,
            'name': '小冰',
            'content': msg
            }
        }
    return node
