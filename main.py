import discord
from discord.ext import commands
import json
import random

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
        description=f'**ОБЩИЕ КОМАНДЫ:**\n\n{prefix}пинг - Проверка работоспособности\n{prefix}хелп - Помощь (текущая команда)\n{prefix}бот - Информация о боте\n\n**УПРАВЛЕНИЕ КАНАЛАМИ И ПОЛЬЗОВАТЕЛЯМИ:**\n\n{prefix}очистить - Очистка сообщений\n{prefix}юзер - Информация о пользователе\n{prefix}пред - Выдать предупреждение пользователю\n{prefix}преды - Предупреждения пользователя',
        color=16705372
    ))

@client.command(aliases=['очистить'])
async def purge(ctx, num=None):
    if num != None:
        await ctx.channel.purge(limit=int(num))
        await ctx.send(embed=discord.Embed(
            title='ОЧИСТКА',
            description=f'Удалено {num} сообщений!',
            color=16705372))
    else:
        await ctx.channel.purge(limit=num)
        await ctx.send(embed=discord.Embed(
            title='ОЧИСТКА',
            description=f'Удалены все сообщения!',
            color=16705372))

@client.command(aliases=['бот'])
async def talk(ctx):
    await ctx.message.reply(embed=discord.Embed(
        title='БОТ',
        description=f'Привет, я {client.user.mention}!\nМоя ссылка-приглашение: https://discord.com/api/oauth2/authorize?client_id=969855185780342854&permissions=8&scope=bot',
        color=16705372))

@client.command(aliases=['юзер'])
async def user(ctx, member: discord.Member = None):
    if member == None:
        await ctx.message.reply(embed=discord.Embed(
            title='ЮЗЕР',
            description=f'**Информация о пользователе {ctx.message.author.mention}:**\nID: {ctx.message.author.id}\nАккаунт создан: {ctx.message.author.created_at}\nПрисоединился: {ctx.message.author.joined_at}\nСсылка на аватар: {ctx.message.author.avatar_url}',
            color=16705372))
    else:
        await ctx.message.reply(embed=discord.Embed(
            title='ЮЗЕР',
            description=f'**Информация о пользователе {member.mention}:**\nID: {member.id}\nАккаунт создан: {member.created_at}\nПрисоединился: {member.joined_at}\nСсылка на аватар: {member.avatar_url}',
            color=16705372))

@client.command(aliases=['пред'])
async def warn(ctx, member: discord.Member):
    with open('warns.json', 'r') as file:
        data = json.load(file)
        if member.id in data:
            with open('warns_id.json', 'r') as tempFile:
                nums = json.load(tempFile)
                num = random.randint(100000, 999999)
                while num in nums:
                    num = random.randint(100000, 999999)
                data[member.id].append(num)
                await ctx.message.reply(embed=discord.Embed(
                    title='ПРЕД',
                    description=f'{member.mention} выдано предупреждение № {num}',
                    color=16705372))
        else:
            with open('warns_id.json', 'r') as tempFile:
                nums = json.load(tempFile)
                num = random.randint(100000, 999999)
                while num in nums:
                    num = random.randint(100000, 999999)
                data[member.id] = [num]
                await ctx.message.reply(embed=discord.Embed(
                    title='ПРЕД',
                    description=f'{member.mention} выдано предупреждение № {num}',
                    color=16705372))
    with open('warns.json', 'w') as file:
        json.dump(data, file)
    with open('warns_id.json', 'w') as file:
        nums.append(num)
        json.dump(nums, file)

@client.command(aliases=['преды'])
async def warns(ctx, member: discord.Member):
    with open('warns.json', 'r') as file:
        data = json.load(file)
        if str(member.id) in data:
            warns = ''
            for i in data[str(member.id)]:
                warns += str(i)
                warns += '\n'
            await ctx.message.reply(embed=discord.Embed(
                    title='ПРЕДЫ',
                    description=f'Предупреждения {member.mention}:\n{warns}',
                    color=16705372))
        else:
            await ctx.message.reply(embed=discord.Embed(
                    title='ПРЕДЫ',
                    description=f'У {member.mention} нет предупреждений',
                    color=16705372))

@client.event
async def on_ready():
    print(f'{client.user.name}#{client.user.id} authorized for:')
    for guild in client.guilds:
        print(guild.name, guild.id)

client.run('OTY5ODU1MTg1NzgwMzQyODU0.G2sMF3.Y8qWvcOQva2ssQq_XkfFL91c8Q1J-ktiJqDYJ8')
