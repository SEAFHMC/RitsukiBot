from PicImageSearch import NetWork, AsyncAscii2D


async def a2d_func(imgs):
    # Using Color
    async with NetWork() as client:
        ascii2d = AsyncAscii2D(client=client, bovw=False)
        res = await ascii2d.search(imgs[0])
    result_color = {
        'thumbnail': res.raw[1].thumbnail,
        'title': res.raw[1].title, 'authors': res.raw[1].authors,
        'url': res.raw[1].url}

    # Using Bovm
    async with NetWork() as client:
        ascii2d = AsyncAscii2D(client=client)
        res = await ascii2d.search(imgs[0])
    result_bovm = {
        'thumbnail': res.raw[1].thumbnail,
        'title': res.raw[1].title, 'authors': res.raw[1].authors,
        'url': res.raw[1].url}

    return [result_color, result_bovm]
