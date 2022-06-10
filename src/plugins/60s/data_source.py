from typing import Optional
from httpx import AsyncClient


async def get_60s() -> Optional[str]:
    url = "https://api.iyk0.com/60s/"
    async with AsyncClient() as client:
        resp = await client.get(url=url)
    if resp.status_code == 200:
        return resp.json()["imageUrl"]
    return None
