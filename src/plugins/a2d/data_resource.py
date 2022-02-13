from PicImageSearch import Ascii2D


async def a2d_func(imgs):
    # Using Color
    ascii2d = Ascii2D(bovw=False)
    res = ascii2d.search(imgs[0])
    result_color = {
        'thumbnail': res.raw[1].thumbnail,
        'title': res.raw[1].title, 'authors': res.raw[1].authors,
        'url': res.raw[1].url}

    # Using Bovm
    ascii2d = Ascii2D()
    res = ascii2d.search(imgs[0])
    result_bovm = {
        'thumbnail': res.raw[1].thumbnail,
        'title': res.raw[1].title, 'authors': res.raw[1].authors,
        'url': res.raw[1].url}

    return [result_color, result_bovm]
