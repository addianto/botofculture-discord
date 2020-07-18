# Bot of Culture _(bot-of-culture)_

> Yet another Discord bot for *cultured* users.

A bot that fetches images from URLs and post the images to a Discord channel.
Currently only supports images from [Pixiv](https://www.pixiv.net) and [Twitter](https://twitter.com/).

## Prerequisites

The following is the requirements for running the bot:

- Python 3.7+ with `venv` built-in module available
  - On Debian-based system, you need to install `python3-venv` separately.
    Example: `sudo apt-get install python3-venv`
- Discord token
- Pixiv credentials (username & password)

## Setup

Fetch the source code to a location in the local filesystem. For example:

```bash
git clone https://github.com/addianto/botofculture-discord.git /opt/botofculture-discord
```

Go to the bot installation folder and initialise the Python virtual
environment:

```bash
cd /opt/botofculture-discord
python -m venv env
source env/bin/activate
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
# Optional: install development-related dependencies
# pip install -r requirements-dev.txt
```

Create `.env` file that contains credentials and bot configuration in the bot
installation folder:

```bash
echo "DEBUG=False" >> .env
echo "DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN" >> .env
echo "PIXIV_USERNAME=YOUR_PIXIV_USERNAME" >> .env
echo "PIXIV_PASSWORD=YOUR_PIXIV_PASSWORD" >> .env
echo "TWITTER_CONSUMER_KEY=YOUR_TWITTER_CONSUMER_KEY" >> .env
echo "TWITTER_CONSUMER_SECRET=YOUR_TWITTER_CONSUMER_SECRET" >> .env
echo "TWITTER_TOKEN_KEY=YOUR_TWITTER_TOKEN_KEY" >> .env
echo "TWITTER_TOKEN_SECRET=YOUR_TWITTER_TOKEN_SECRET" >> .env
```

Run the bot manually:

```bash
python botofculture.py
# CTRL-C to terminate the bot
```

If you want to run the bot in background, please run it under `screen` or
`tmux` session. Alternatively, you can also setup a `systemd` service that
will run the bot as a service. An example of `systemd` configuration file
is available in [`deploy/`](deploy/botofculture-discord.service) directory.

## Credits

This project is heavily influenced by [`saucebot-discord`](https://github.com/JeremyRuhland/saucebot-discord).
The functionality is similar, but this project fetches and shows all images
instead of only showing the first image in the collection when given a Pixiv
artwork that contains multiple images.

## License

This project is licensed under [MIT](LICENSE).
