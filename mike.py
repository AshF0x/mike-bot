import discord
from discord.ext import commands
import time
import os
import logging

TOKEN = os.getenv('DISCORD_API_TOKEN')

# Debug Logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='mike.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asciitime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!')
initial_extensions = [
    'cogs.facts', 
    'cogs.thm'
]

if __name__ == '__main__':
    for extensions in initial_extensions:
        bot.load_extension(extensions)

@bot.event
async def on_ready():
    print('Bot Startup at ' + time.strftime('%c'))
    print('We have logged in as User ', bot.user)
    print('............')
    print('Mike is live')
    print('............')

bot.run(TOKEN, bot=True)