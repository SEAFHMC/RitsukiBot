from nonebot import on_notice, NoticeSession
import nonebot


@on_notice('group_recall')
async def _(session: NoticeSession):
    bot = nonebot.get_bot()
    message_id = session.ctx['message_id']
    group_id = session.ctx['group_id']
    user_id = session.ctx['user_id']
    operator_id = session.ctx['operator_id']
    if operator_id == user_id:
        member_info = await bot.get_group_member_info(group_id=group_id, user_id=user_id)
        nickname = member_info['nickname']
        recalled_msg_all = await bot.get_msg(message_id=message_id)
        recalled_msg_content = recalled_msg_all['raw_message']
        result = nickname+"撤回了一条消息："+"\n"+recalled_msg_content
        await bot.send_group_msg(group_id=group_id, message=result)
