from .function import check_update, get_update, strip_deco, get_img_url
import nonebot
from nonebot import MessageSegment
from time import sleep
from data_resource import rss_list, group_list


@nonebot.scheduler.scheduled_job('interval', minutes=10)
async def _():
    bot = nonebot.get_bot()
    for i in rss_list:
        try:
            bool = await check_update(i)
        except FileNotFoundError:
            bool = True
        if bool is True:
            jsons_dict = await get_update(i)
            if i == 'gf-cn/news':
                result = '少女前线火星新闻：\n'+jsons_dict['title']
            elif i == 'epicgames/freegames':
                summary = await strip_deco(jsons_dict['summary'])
                img_url = await get_img_url(jsons_dict['summary'])
                result = 'Epic商城有新游戏可领取：\n'+jsons_dict['title']+'\n'+summary+'\n'+MessageSegment.image(img_url)+jsons_dict['id']
            elif i == 'bilibili/user/dynamic/404145357':
                img_url = await get_img_url(jsons_dict['summary'])
                summary = await strip_deco(jsons_dict['summary'])
                result = 'Arcaea火星新闻：\n'+summary+MessageSegment.image(img_url)
            for j in group_list:
                sleep(5)
                await bot.send_group_msg(group_id=j, message=result)
