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
}


def get(key: str):
    return config[key]
