from nonebot.plugin import on_message
from nonebot.params import EventPlainText
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from .rule import enable_group
from .chat_recorder import ChatRecorder

monitor = on_message(rule=enable_group)


@monitor.handle()
async def _(event: GroupMessageEvent, message: str = EventPlainText()):
    ChatRecorder.write(
        user_id=event.user_id,
        group_id=event.group_id,
        message=message,
        timestamp=event.time,
    )
