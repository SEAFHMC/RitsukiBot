import ujson as json
import httpx
from typing import List


def get_message_img(data: str) -> List[str]:
    """
    说明：
        获取消息中所有的 图片 的链接
    参数：
        :param data: event.json()
    """
    try:
        img_list = []
        data = json.loads(data)
        for msg in data["message"]:
            if msg["type"] == "image":
                img_list.append(msg["data"]["url"])
        return img_list
    except KeyError:
        return []


async def httpx_request(url: str) -> str:
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
    return res.text
