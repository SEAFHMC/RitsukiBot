from pydantic import BaseModel, Extra
from nonebot import get_driver
from typing import List


class Config(BaseModel, extra=Extra.ignore):
    wordcloud_enable_group: List[int] = []

plugin_config = Config.parse_obj(get_driver().config)