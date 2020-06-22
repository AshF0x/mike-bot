import discord
from discord.ext import commands
import requests
import json

class thm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='!thm', description='Prints out THM stats')
    async def thm(self, ctx, arg):
        user = str(arg)
        r = requests.get('https://tryhackme.com/api/user/'+ user )
        all_stats = r.json()
        rank = all_stats['userRank']
        beddy = discord.Embed(type='rich', title='Current rank of "'+ user +'" on THM', color=0xD68910)
        beddy.add_field(name='Rank', value=rank, inline=False)
        await ctx.send(embed=beddy)

def setup(bot):
    bot.add_cog(thm(bot))