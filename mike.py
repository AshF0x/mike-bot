import discord
import os
import random
import time

# Loading Token, Set your personal Token as env variable "DISCORD_API_TOKEN"
TOKEN = os.getenv("DISCORD_API_TOKEN")
client = discord.Client()

file = open('facts.txt','r')
facts = file.read().splitlines()
file.close()

# Loading Message in cli
@client.event
async def on_ready():
    print('Bot Startup at ' + time.strftime('%c'))
    print('We have logged in as User ', client.user)
    print('............')
    print('Mike is live')
    print('............')

# Fly Facts
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!fact'):
        fact = random.choice(facts)
        await message.channel.send(fact)


client.run(TOKEN)