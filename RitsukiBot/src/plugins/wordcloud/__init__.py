from nonebot.plugin import on_message
from .rule import enable_group

monitor = on_message(rule=enable_group)