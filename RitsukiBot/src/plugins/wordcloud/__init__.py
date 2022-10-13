from nonebot.plugin import on_message, on_command
from nonebot.params import EventPlainText
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from time import time
from .data_source import enable_group, format_time
from .chat_recorder import ChatRecorder
from .config import plugin_config

monitor = on_message(rule=enable_group, block=False)


@monitor.handle()
async def _(event: GroupMessageEvent, message: str = EventPlainText()):
    ChatRecorder.write_record(
        user_id=event.user_id,
        group_id=event.group_id,
        message=message,
        date=format_time(event.time),
    )


generate = on_command("生成今日词云", aliases={"生成词云"})


@generate.handle()
async def _(event: GroupMessageEvent):
    if event.group_id in plugin_config.wordcloud_enable_group:
        await generate.finish(
            MessageSegment.image(
                ChatRecorder.generate_wordcloud(
                    date=format_time(time()), group_id=event.group_id
                )
            )
        )
    await generate.finish("该群未启用词云")
