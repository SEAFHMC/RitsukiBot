from utils.utils import open_img_from_url
from nonebot_plugin_imageutils import Text2Image
from PIL import Image
from numpy import average
from typing import Tuple
from io import BytesIO


def get_average_color(image: Image.Image, pos: Tuple[int, int]):
    pix = image.load()
    R_list = []
    G_list = []
    B_list = []
    for x in range(pos[0]):
        for y in range(pos[1]):
            R_list.append(pix[x, y][0])
            G_list.append(pix[x, y][1])
            B_list.append(pix[x, y][2])
    R_average = int(average(R_list))
    G_average = int(average(G_list))
    B_average = int(average(B_list))
    return (R_average, G_average, B_average)


def is_dark(color: Tuple[int, int, int]):
    return (
        True if color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114 < 192 else False
    )


async def enhanced_setu(url: str, pid: int):
    url = url.replace("https://i.pximg.net/", "http://127.0.0.1:17777/pixiv/")
    img = await open_img_from_url(url)
    font_size = int(img.height / 32)
    text = Text2Image.from_text(text=f"Pixiv | {pid}", fontsize=font_size).to_image()
    text_pos = (img.width - text.width, img.height - text.height)
    fill = "white" if is_dark(get_average_color(img, text_pos)) else "black"
    text = Text2Image.from_text(
        text=f"Pixiv | {pid}", fontsize=font_size, fill=fill
    ).to_image()
    img.alpha_composite(text, text_pos)
    buffer = BytesIO()
    img.save(buffer, "png")
    return buffer
