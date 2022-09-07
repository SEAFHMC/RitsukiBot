from httpx import AsyncClient
from nonebot.adapters.onebot.v11.message import MessageSegment
from .schema import Model


async def get_epic():
    url = "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN"
    async with AsyncClient(timeout=100) as client:
        resp = await client.get(url=url)

    raw_data = Model(**resp.json())
    game_list = raw_data.data.Catalog.searchStore.elements
    game_list = list(filter(lambda x: x.promotions, game_list))
    present = list(filter(lambda x: x.promotions.promotionalOffers, game_list))  # type: ignore
    next = list(filter(lambda x: x.promotions.upcomingPromotionalOffers, game_list))  # type: ignore
    return (present, next)


async def make_msg():
    (present, next) = await get_epic()
    msg = []
    for game in present:
        msg += MessageSegment.text(f"即刻在Epic商城领取{game.title}\n")
        msg += MessageSegment.image(game.keyImages[0].url)
        msg += MessageSegment.text(f"\n{game.description}\n")
    msg += MessageSegment.text(f"下周可白嫖{'和'.join([i.title for i in next])}")
    return msg
