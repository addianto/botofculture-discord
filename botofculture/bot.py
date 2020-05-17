import discord
import logging
import sys
client = discord.Client()


@client.event
async def on_error(event: str, *args, **kwargs):
    logging.exception(msg=event,
                      args=args,
                      exc_info=sys.exc_info(),
                      stack_info=True)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    logging.debug(f'{message.author.name}: {message.content}')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user.name} with ID {client.user.id}')


def run(token: str):
    client.run(token)
