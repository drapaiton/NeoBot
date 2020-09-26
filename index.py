#!/usr/bin/ python3
# -*- coding: <utf8> -*-
import os
from decouple import config as envConf
import discord
from utils import default
from utils.data import NeoBot, HelpFormat

if __name__ == "__main__":
    config = default.get("config.json")
    print("Logging in...")

    bot = NeoBot(
        command_prefix=config.prefix,
        prefix=config.prefix,
        command_attrs=dict(hidden=True),
        help_command=HelpFormat(),
        fetch_offline_members=False,
        description=config.description,
        allowed_mentions=discord.mentions.AllowedMentions(
        everyone=False, users=True, roles=False), 
    )

    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            bot.load_extension(f"cogs.{name}")

    bot.remove_command('help')

    try:
        bot.run(envConf("TOKEN"))
    except Exception as e:
        print(f'Error when logging in: {e}')
