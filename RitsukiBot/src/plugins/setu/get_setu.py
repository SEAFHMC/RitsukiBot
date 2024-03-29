from typing import Literal
from httpx import AsyncClient
from .schema import SetuJson


class Setu:
    base_url = "https://api.ritsuki.top/setu"

    @classmethod
    async def _quick_get(cls, url: str):
        async with AsyncClient() as client:
            return await client.get(url=url)

    @classmethod
    async def get_setu(cls, tag: str = '"', r18: Literal[0, 1, 2] = 0, number: int = 1):
        url = f"{cls.base_url}/search?r18={r18}&tag={tag}&number={number}"
        resp = await cls._quick_get(url=url)
        return SetuJson(**resp.json())
