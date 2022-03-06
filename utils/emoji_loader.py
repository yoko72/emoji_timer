import discord
from discord.ext.commands import command, Cog
from functools import lru_cache


class EmojiLoaderCog(Cog):
    def __init__(self, bot, id_of_guild: int):
        super().__init__()
        self.bot = bot
        self.__id_of_emoji_storage_guild = id_of_guild

    @property
    @lru_cache()
    def guild_storing_emoji(self):
        return self.bot.get_guild(self.__id_of_emoji_storage_guild)

    def get_emoji(self, emoji_name):
        return discord.utils.get(self.bot.emojis, name=emoji_name, guild=self.guild_storing_emoji)


