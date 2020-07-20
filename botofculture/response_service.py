import logging
from pathlib import Path
from . import config

import discord


async def send_image(message: discord.Message, image_file: Path,
                     is_nsfw: bool):
    if not image_file.exists():
        return

    logging.debug(f'Sending {image_file} to {message.channel.name} at {message.channel.guild.name}')  # noqa
    await message.channel.send(file=discord.File(str(image_file),
                                                 spoiler=is_nsfw))

    logging.debug(f'Removing {image_file} from the local cache')
    image_file.unlink()


def create_image_folder_if_not_exists():
    storage_dir = Path(config.get("DOWNLOAD_PATH"))

    if not storage_dir.exists():
        storage_dir.mkdir()
