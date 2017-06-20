import discord

from discord.ext import commands

description = 'Discord bot coded in python made by Yu Xiu'
bot_prefix = 'm!'

client = commands.Bot(description=description, command_prefix=bot_prefix)


@client.event
async def on_ready():
     print('Online!')
     print('Name : {}'.format(client.user.name))
     print('ID : {}'.format(client.user.id))

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_member_remove(member):
    server = member.server
    fmt = 'Goodbye {0.mention} has just left {1.name}!'
    await client.send_message(server, fmt.format(member, server))



@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('c!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        message.delete();


    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('key 1239192391391293984375494031837126y45394312031834576y5thgfndjmsk,LCIUNFSAIDMEUJDIA'):
       addRole('162459498043277312')


@client.command(pass_context=True)
async def ping(ctx):
     await client.say('Pong!')


client.run('MzIwNTM4NzkwODQ0MzAxMzEz.DCSLhQ.A2ojoXQA2f2tWN1ZvEEXLKoH0pQ')
