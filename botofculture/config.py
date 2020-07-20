from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
config = {
    'DEBUG': True if os.getenv('DEBUG', 'False') == 'True' else False,
    'DISCORD_TOKEN': os.getenv('DISCORD_TOKEN'),
    'DOWNLOAD_PATH': os.getenv('DOWNLOAD_PATH',
                               os.path.join(os.path.curdir, 'files')),
    'PIXIV_USERNAME': os.getenv('PIXIV_USERNAME'),
    'PIXIV_PASSWORD': os.getenv('PIXIV_PASSWORD'),
    'TWITTER_CONSUMER_KEY': os.getenv('TWITTER_CONSUMER_KEY'),
    'TWITTER_CONSUMER_SECRET': os.getenv('TWITTER_CONSUMER_SECRET'),
    'TWITTER_TOKEN_KEY': os.getenv('TWITTER_TOKEN_KEY'),
    'TWITTER_TOKEN_SECRET': os.getenv('TWITTER_TOKEN_SECRET')
}


def get(key: str):
    return config[key]
