from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
config = {
    'DEBUG': True if os.getenv('DEBUG', 'False') == 'True' else False,
    'DISCORD_TOKEN': os.getenv('DISCORD_TOKEN'),
    'PIXIV_USERNAME': os.getenv('PIXIV_USERNAME'),
    'PIXIV_PASSWORD': os.getenv('PIXIV_PASSWORD'),
}


def get(key: str):
    return config[key]
