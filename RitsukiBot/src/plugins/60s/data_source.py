from typing import Optional
from httpx import AsyncClient


async def get_60s() -> Optional[str]:
    url = "https://api.2xb.cn/zaob"
    async with AsyncClient() as client:
        resp = await client.get(url=url)
    if resp.status_code == 200:
        return resp.json()["imageUrl"]
    return None
