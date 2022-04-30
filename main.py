import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command('ping')
client.remove_command('help')

@client.command()
async def ping(ctx):
    await ctx.send(embed=discord.Embed(
        title='PING',
        description='PONG!',
        color=16705372
    ))

@client.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(
        title='HELP',
        description='help',
        color=16705372
    ))

@client.event
async def on_ready():
    print(f'{client.user.name}#{client.user.id} authorized for:')
    for guild in client.guilds:
        print(guild.name, guild.id)

client.run('OTY5ODU1MTg1NzgwMzQyODU0.YmzeBw.3DWzsX1ItsKSO_6LMrNeOQhD4Sc')