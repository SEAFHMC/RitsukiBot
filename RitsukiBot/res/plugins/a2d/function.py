from PicImageSearch import Ascii2D


async def a2d(CQcode):
    for i in range(len(CQcode)):
        if CQcode[i:i+3] == 'url':
            img_url = CQcode[i+4:-1]
# Using Color
    ascii2d = Ascii2D(bovw=False)
    res = ascii2d.search(img_url)
    result_color = {
        'thumbnail': res.raw[1].thumbnail,
        'title': res.raw[1].title, 'authors': res.raw[1].authors,
        'url': res.raw[1].url}

# Using Bovm
    ascii2d = Ascii2D()
    res = ascii2d.search(img_url)
    result_bovm = {
        'thumbnail': res.raw[1].thumbnail,
        'title': res.raw[1].title, 'authors': res.raw[1].authors,
        'url': res.raw[1].url}

    return [result_color, result_bovm]
