# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
import time
from itertools import cycle
from discord.utils import get
from discord import Game
import os

client = commands.Bot(command_prefix='!')
#client = discord.Client()
Clientdiscord = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['!info', '!info', '!info', '!info'])

client.remove_command('help')


@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
        
    if message.content.startswith('!info'):
        msg = 'The bot is now in maintenance, we working on it and we hping that in 3 days bot will work!'
        await message.author.send(msg)

    if message.content.startswith('!help'):
        msg = 'The bot is now in maintenance, we working on it and we hping that in 3 days bot will work!'.format(message)
        await message.author.send(msg)

    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(os.getenv('BOT_TOKEN'))
