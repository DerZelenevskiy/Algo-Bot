import discord
from discord.ext import commands
import os
import sys
import json

prefix = '!'
global client
client = commands.Bot(command_prefix=prefix)
client.remove_command('ping')
client.remove_command('help')

@client.command(aliases=['пинг'])
async def ping(ctx):
    await ctx.message.reply(embed=discord.Embed(
        title='ПИНГ',
        description='Понг!',
        color=16705372
    ))

@client.command(aliases=['хелп'])
async def help(ctx):
    await ctx.message.reply(embed=discord.Embed(
        title='ХЕЛП',
        description=f'**ОБЩИЕ КОМАНДЫ:**\n{prefix}пинг - Проверка работоспособности\n{prefix}хелп - Помощь (текущая команда)\n{prefix}очистить - Очистка сообщений',
        color=16705372
    ))

@client.command(aliases=['очистить'])
async def purge(ctx, num=None):
    if num != None:
        await ctx.channel.purge(limit=int(num))
        await ctx.message.reply(embed=discord.Embed(
            title='ОЧИСТКА',
            description=f'Удалено {num} сообщений!',
            color=16705372))
    else:
        await ctx.channel.purge(limit=num)
        await ctx.message.reply(embed=discord.Embed(
            title='ОЧИСТКА',
            description=f'Удалены все сообщения!',
            color=16705372))

@client.command(aliases=['бот'])
async def talk(ctx):
    await ctx.message.reply(embed=discord.Embed(
        title='БОТ',
        description=f'Привет, я {client.user.mention}!',
        color=16705372))

@client.command(aliases=['рестарт'])
async def restart(ctx):
    await ctx.message.reply(embed=discord.Embed(
        title='РЕСТАРТ',
        description=f'Бот перезапустится через несколько секунд!',
        color=16705372))
    data = {'restart' : [True, ctx.message.channel.id]}
    with open('runtime.json', 'w') as file:
        json.dump(data, file)
    os.startfile(__file__)
    sys.exit()


@client.event
async def on_ready():
    print(f'{client.user.name}#{client.user.id} authorized for:')
    for guild in client.guilds:
        print(guild.name, guild.id)

client.run('OTY5ODU1MTg1NzgwMzQyODU0.YmzeBw.-Zfdw47tPAiKnOAtNU3TSmojIa8')