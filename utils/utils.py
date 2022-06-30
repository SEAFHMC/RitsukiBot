import httpx
from typing import Optional





async def httpx_get(url: str) -> Optional[str]:
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url)
            return res.text
        except Exception:
            return None


