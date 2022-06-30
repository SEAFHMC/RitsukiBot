from typing import Literal
from httpx import AsyncClient
from .schema import SetuJson


class Setu:
    base_url = "http://127.0.0.1:61658/setu"

    @classmethod
    async def _quick_get(cls, url: str):
        async with AsyncClient() as client:
            return await client.get(url=url)

    @classmethod
    async def random_setu(cls, r18: Literal[0, 1, 2] = 0):
        url = f"{cls.base_url}/random.json?r18={r18}"
        resp = await cls._quick_get(url=url)
        return SetuJson(**resp.json())

    @classmethod
    async def search_setu(cls, tag: str, r18: Literal[0, 1, 2] = 0):
        url = f"{cls.base_url}/search?r18={r18}&tag={tag}"
        resp = await cls._quick_get(url=url)
        return SetuJson(**resp.json())
