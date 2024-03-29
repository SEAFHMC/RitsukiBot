from nonebot.plugin import require

require("nonebot_plugin_imageutils")

from utils.utils import open_img_from_url
from nonebot_plugin_imageutils import Text2Image
from PIL import Image
from numpy import average, minimum
from typing import Tuple
from io import BytesIO
from random import randint


def get_average_color(image: Image.Image, pos: Tuple[int, int]):
    pix = image.load()
    R_list = []
    G_list = []
    B_list = []
    width, height = image.size
    for x in range(pos[0], width):
        for y in range(pos[1], height):
            R_list.append(pix[x, y][0])  # type: ignore
            G_list.append(pix[x, y][1])  # type: ignore
            B_list.append(pix[x, y][2])  # type: ignore
    R_average = int(average(R_list))
    G_average = int(average(G_list))
    B_average = int(average(B_list))
    return (R_average, G_average, B_average)


def is_dark(color: Tuple[int, int, int]):
    return (
        True if color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114 < 192 else False
    )


async def enhanced_setu(url: str, pid: int):
    url = url.replace("https://i.pximg.net/", "https://setu.ritsuki.top/")
    img = await open_img_from_url(url)
    font_size = int(minimum(img.width, img.height) / 32)  # type: ignore
    text = Text2Image.from_text(
        text=f"Pixiv | {pid}", fontsize=font_size, fontname="Kazesawa-Regular"
    ).to_image()
    text_pos = (img.width - text.width, img.height - text.height)  # type: ignore
    fill = (
        (255 - randint(0, 50), 255 - randint(0, 50), 255 - randint(0, 50))
        if is_dark(get_average_color(img, text_pos))  # type: ignore
        else (randint(0, 50), randint(0, 50), randint(0, 50))
    )
    text = Text2Image.from_text(
        text=f"Pixiv | {pid}",
        fontsize=font_size,
        fill=fill,
        fontname="Kazesawa-Regular",
    ).to_image()
    img.alpha_composite(text, text_pos)  # type: ignore
    buffer = BytesIO()
    img.convert("RGB").save(buffer, "jpeg")  # type: ignore
    return buffer
