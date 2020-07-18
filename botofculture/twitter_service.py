import os
import re
from pathlib import Path

import twitter
import wget
import discord

from . import config
from .response_service import send_image

TWITTER_CONSUMER_KEY = config.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = config.get('TWITTER_CONSUMER_SECRET')
TWITTER_TOKEN_KEY = config.get('TWITTER_TOKEN_KEY')
TWITTER_TOKEN_SECRET = config.get('TWITTER_TOKEN_SECRET')

TWITTER_URL_PATTERN = re.compile(r'https://twitter.com\/.*status\/(\d*)')

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_TOKEN_KEY, access_token_secret=TWITTER_TOKEN_SECRET)


async def handle(message: discord.message):
    statuses_id = TWITTER_URL_PATTERN.findall(message.content)

    if not statuses_id:
        return
    statuses_data = []
    for status_id in statuses_id:
        try:
            statuses_data.append(await get_status_data(status_id))
        except:
            return

    print(statuses_data)
    for status_data in statuses_data:
        medias = status_data.get('media')
        for media in medias:
            file_url = media.get('media_url_https')
            await parse_image(file_url, message)


async def get_status_data(status_id):
    tweet_detail = api.GetStatus(status_id=status_id).AsDict()
    if tweet_detail['media']:
        return tweet_detail


async def parse_image(file_url, message: discord.message):
    file_path = download_image(file_url)
    async with message.channel.typing():
        await send_image(message, file_path, False)


def download_image(url: str):
    file_name = wget.download(url, config.get('DOWNLOAD_PATH'))
    return Path(os.path.abspath(file_name))
