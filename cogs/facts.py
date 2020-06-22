import discord
from discord.ext import commands
import random
import os

class facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='!fact', description='Mike gives you an interesting fact about flies')
    async def fact(self, ctx):
        file = open('facts.txt','r')
        list = file.read().splitlines()
        file.close()
        answer = random.choice(list)
        await ctx.send(answer)

def setup(bot):
    bot.add_cog(facts(bot))