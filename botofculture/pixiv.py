from . import config
from pathlib import Path
import discord
import logging
import pixivpy_async
import re

PIXIV_URL_PATTERN = re.compile(r'pixiv.net\/.*artworks\/(\d*)')
PIXIV_IMG_URL_PATTERN = re.compile(r'i\.pximg\.net\S*\w')
api = pixivpy_async.PixivAPI()


def get_image_urls(work: dict) -> list:
    logging.debug(f'Parsing image URLs from: {work}')

    if work.page_count == 1:
        return [work.image_urls.large]
    else:
        pages = work.metadata.pages
        return [page.image_urls.large for page in pages]


async def handle(message: discord.Message):
    work_ids = PIXIV_URL_PATTERN.findall(message.content)

    if not work_ids:
        return

    await api.login(config.get('PIXIV_USERNAME'),
                    config.get('PIXIV_PASSWORD'))

    works = map(lambda json: json.response[0],
                filter(lambda json: json.status == 'success',
                       [await api.works(id) for id in work_ids]))

    for work in works:
        image_urls = get_image_urls(work)

        await message.channel.send(f'''
            **Title**: {work.title}
            **Author**: {work.user.name}
            **Tags**: {', '.join(work.tags)}
        ''')

        for url in image_urls:
            filename = url.rsplit('/', 1)[-1]
            downloaded_file = await download_image(url, filename,
                                                   config.get('DOWNLOAD_PATH'))

            async with message.channel.typing():
                await send_image(message, downloaded_file)


async def download_image(url: str, filename: str, path: str):
    # TODO Store the image to in-memory cache instead of filesystem
    #      (need to modify Pixiv API)
    storage_dir = Path(path)
    image_file = storage_dir.joinpath(filename)

    if not storage_dir.exists():
        storage_dir.mkdir()

    if not image_file.exists():
        logging.debug(f'Downloading {url} to {str(image_file)}')
        await api.download(url, fname=filename, path=path)

    return image_file


async def send_image(message: discord.Message, image_file: Path):
    if not image_file.exists():
        return

    logging.debug(f'Sending {image_file} to {message.channel.name} at {message.channel.guild.name}')  # noqa
    await message.channel.send(file=discord.File(str(image_file)))
    image_file.unlink()
