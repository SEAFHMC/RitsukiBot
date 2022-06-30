from httpx import AsyncClient
from typing import Optional
from PIL import Image
from io import BytesIO


async def httpx_get(url: str) -> Optional[str]:
    async with AsyncClient() as client:
        try:
            res = await client.get(url)
            return res.text
        except Exception:
            return None


async def open_img_from_url(url: str) -> Optional[Image.Image]:
    try:
        async with AsyncClient() as client:
            resp = await client.get(url)
        return Image.open(BytesIO(resp.read())).convert("RGBA")
    except Exception:
        return None
