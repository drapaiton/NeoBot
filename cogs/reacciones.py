#!/usr/bin/ python3
# -*- coding: <utf8> -*-
from discord.ext import commands
import discord
import re


class ReaccionesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """Priority speed over readage"""
        if(message.author.id == self.bot.mee6):
            #level < 10
            if re.match(""".*([0-9]!)$""", message.content):
                kpequeno = discord.utils.get(
                    self.bot.guild.emojis, name="kpequeno")
                await message.add_reaction(kpequeno)

            # level [1-9] one or more, and one or more 0
            elif re.match(""".*([1-9]+0+!)$""", message.content):
                kgrande = discord.utils.get(
                    self.bot.guild.emojis, name="kgrande")
                await message.add_reaction(kgrande)


def setup(bot):
    bot.add_cog(ReaccionesCog(bot))
