from pathlib import Path
from typing import Optional, Union
from PIL import ImageDraw, ImageFont, Image


ROOT = Path().resolve() / "RitsukiBot" / "data" / "fonts"
ROOT.mkdir(parents=True, exist_ok=True)
gb_2312 = ROOT / "仿宋_GB2312.ttf"


def combine_img(*imgs: Image.Image):
    width_limit = max([i.width for i in imgs])
    height_limit = sum([i.height for i in imgs])
    img = Image.new("RGBA", (width_limit, height_limit), (255, 255, 255, 0))
    y = 0
    for i in imgs:
        img.alpha_composite(i, (0, y))
        y += i.height
    return img


class Text2Image:
    @staticmethod
    def from_text(
        text: str,
        font_path: Union[str, Path],
        font_size: int = 12,
        width_limit: Optional[int] = None,
    ):
        true_font = ImageFont.truetype(font=str(font_path), size=font_size)

        def draw_text(text: str):
            (lt, lb, rt, rb) = true_font.getbbox(text)
            text_overlay = Image.new("RGBA", (rt, rb), (255, 255, 255, 0))
            image_draw = ImageDraw.Draw(text_overlay)
            image_draw.text(xy=(0, 0), text=text, fill="black", font=true_font)
            return text_overlay

        if not width_limit:
            return draw_text(text=text)
        text_list = [text]
        while True:
            if draw_text(text[0]).width > width_limit:
                print("Text Too Long!")
            tail = text_list[-1]
            for i in range(0, len(tail)):
                if draw_text(tail[:i]).width > width_limit:
                    del text_list[-1]
                    text_list.append(tail[:i])
                    text_list.append(tail[i:])
                    break
            if draw_text(text_list[-1]).width < width_limit:
                break
        return combine_img(*[draw_text(i) for i in text_list])
