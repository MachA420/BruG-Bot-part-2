#BruG Bot

import random
import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '*')
status = cycle(['BruG Bot! *help', 'Franco is gay', 'Eric is an Eggbrain.', 'Can i?', 'Meeboop clan!', 'EGGBRAIN ON TOP!', 'Log is gay', 'The woods is faggotery server', 'Bannaa', ''])

@client.event
async def on_ready():
    change_status.start()
    print('The Bot is Ready my bro.')

#User Joined the server
@client.event
async def on_member_join(member):
    print(f'{member} has joined BruG.')

#User left the server
@client.event
async def on_member_remove(member):
    print(f'{member} has left BruG.')

@client.command()
async def ping(ctx):
    await ctx.send(f'wassup {round(client.latency * 1000)}ms')

@client.command(aliases=['8Ball', '69ball'])
async def _69Ball(ctx, *, question):
    responses = ['Yessir on jah.',
                 'Most likely my jigga.',
                 'Probably yo.',
                 'Fr.',
                 'Hell yeh',
                 'Yessir she wants to do it',
                 'Stay wit it itll be worth it.',
                 'Nah homie.',
                 'Nah youre gay.',
                 'HELL NAH.',
                 'I doubt it my meeboo.',
                 'Dont go for it.',
                 'Fuck you.',
                 'No.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
#kicks a memeber
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from BruG')

#bans a user with a reason
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from BruG')

#Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension()

#BG Tasks
@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#hello
@client.command()
async def hello(ctx):
    await ctx.send(f'Hello! :)')

#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please type the command properly.')

#Whitelist
def is_it_me(ctx):
    return ctx.author.id == 317700007006306304

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi im {ctx.author}')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.ass_roles(member, role)

@client.command()
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You need to be in a voice channel for me to join!")

@client.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in a voice channel")


client.run('ODQ3Njc3MTI3NTk1MjYxOTgy.YLBi2A.3_Y-A6_kKXPLKF1X9D5pf7Q0Jd8')