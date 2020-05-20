from . import config
import aiohttp
import discord
import io
import logging
import pixivpy_async
import re

PIXIV_URL_PATTERN = re.compile(r'pixiv.net\/.*artworks\/(\d*)')
PIXIV_IMG_URL_PATTERN = re.compile(r'i\.pximg\.net\S*\w')
PIXIV_API_URL = 'https://app-api.pixiv.net/'
papi = pixivpy_async.PixivAPI()
session = aiohttp.ClientSession()


async def login():
    return await papi.login(config.get('PIXIV_USERNAME'),
                            config.get('PIXIV_PASSWORD'))


async def handle(message: discord.Message):
    work_ids = PIXIV_URL_PATTERN.findall(message.content)

    if not work_ids:
        return

    # TODO Do something with access_token and refresh_token?
    await login()

    works = map(lambda json: json.response[0],
                filter(lambda json: json.status == 'success',
                       [await papi.works(id) for id in work_ids]))

    for work in works:
        image_urls = get_image_urls(work)

        for url in image_urls:
            async with session.get(url, headers={'Referer': PIXIV_API_URL}) as response:  # noqa
                raw_image = await get_image(response)
                raw_image.name = url.rsplit('/', 1)[-1]

                async with message.channel.typing():
                    await message.channel.send(file=discord.File(raw_image))


def get_image_urls(work: dict) -> list:
    logging.debug(f'Parsing image URLs from: {work}')

    if work.page_count == 1:
        return [work.image_urls.large]
    else:
        pages = work.metadata.pages
        return [page.image_urls.large for page in pages]


async def get_image(response: aiohttp.ClientResponse):
    buffer = b''

    async for data, _ in response.content.iter_chunks():
        buffer += data

    return io.BytesIO(buffer)
