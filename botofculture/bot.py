from . import pixiv
import discord
import logging
import sys
client = discord.Client()


@client.event
async def on_error(event: str, *args, **kwargs):
    logging.error(f'Encountered error on event {event}',
                  exc_info=sys.exc_info(),
                  stack_info=True)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    logging.debug(f'{message.author.name} AKA {message.author.display_name} at {message.guild.name}')  # noqa
    logging.debug(f'> {message.content}')

    await pixiv.handle(message)


@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user.name} with ID {client.user.id}')
    logging.info(f'Member of the following guild(s): {client.guilds}')


def run(token: str):
    client.run(token)
