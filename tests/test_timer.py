
from os import environ
import unittest
import asyncio

import discord
from discord.ext.commands import Bot, Cog

from src.emoji_timer import EmojiTimerCog

PREFIX = "!"

# set following 4 strings as your environment var

GUILD_ID_FOR_EMOJIS = "GUILD_ID_FOR_EMOJIS"
GUILD_ID_TO_TEST = "GUILD_ID_TO_TEST"
CHANNEL_ID_TO_TEST = "CHANNEL_ID_TO_TEST"
ENV_VAR_NAME_FOR_TOKEN = "TEST_BOT_TOKEN"


intents = discord.Intents.all()
bot = discord.ext.commands.Bot(PREFIX, intents=intents)


class AutoTimerCommandCog(EmojiTimerCog):

    @EmojiTimerCog.listener()
    async def on_ready(self):
        print("on_ready!")
        test_server = discord.utils.get(self.bot.guilds, id=int(environ[GUILD_ID_TO_TEST]))
        test_channel = discord.utils.get(test_server.channels, id=int(environ[CHANNEL_ID_TO_TEST]))
        await self.countdown(channel=test_channel, minutes=10)

bot.add_cog(AutoTimerCommandCog(bot, int(environ[GUILD_ID_FOR_EMOJIS])))
token = environ[ENV_VAR_NAME_FOR_TOKEN]
bot.run(token)
