'''
A Discord bot named "Bot of Culture".
'''
__title__ = 'botofculture-discord'
__author__ = 'addianto'
__copyright__ = f'Copyright (c) 2020 {__author__}'
__license__ = 'MIT'
__version__ = '0.2.0'

from . import bot, config
import logging

DEBUG = config.get('DEBUG')
DISCORD_TOKEN = config.get('DISCORD_TOKEN')

logging.basicConfig(
    datefmt='%Y-%m-%dT%H:%M:%S%z',
    format='%(asctime)s | %(levelname)s | %(name)s | %(filename)s#%(funcName)s()#L%(lineno)d | %(message)s',  # noqa
    level=logging.DEBUG if DEBUG else logging.INFO
)


def run():
    logging.info(f'You are running {__title__} v{__version__}')
    logging.info(f'Debug mode: {"enabled" if DEBUG else "disabled"}')
    bot.run(DISCORD_TOKEN)
