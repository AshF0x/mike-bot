import discord
from discord.ext import commands

class users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Prints the current users on the server
    @commands.command(brief='!users', description='Prints the current number of Users')
    async def users(self, ctx):
        users = str(ctx.guild.member_count)
        await ctx.send(f'Current users on F0xBox:🦊{users}')
# Updates The designated VC to reflect the current user numbers
    @commands.has_role('admin')
    @commands.command()
    async def channel(self, ctx):
        for channel in ctx.guild.channels:
            if channel.id == 724626660325982268:
                users = str(ctx.guild.member_count)
                await channel.edit(name=f'🦊Foxes: {users}')
                print('IT IS THE PERMISSIONS NOOBY')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.get_channel(724626660325982268)
        users = self.bot.guild.member_count
        await channel.edit(name=f'🦊Foxes: {users}')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.get_channel(724626660325982268)
        users = self.bot.guild.member_count
        await channel.edit(name=f'🦊Foxes: {users}')
    

def setup(bot):
    bot.add_cog(users(bot))