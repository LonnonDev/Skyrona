"""
MIT License

Copyright (c) 2020 LonnonjamesD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
import json
import random
import math
import discord
import os
import sys
import sqlite3
import secret
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from os import listdir
import datetime
import asyncio
# import the token
from config import *

# Changes the directory to this file's parent folder
os.chdir('F:/Skyrona')

def printl(string):
	prn = open("F:/Skyrona/output.txt", 'a')
	prn.write(f'\n{string}')
	prn.close()
	print(string)


# Connects to the database
conn = sqlite3.connect("people.db")
c = conn.cursor()

# Create a table if does not exist people
c.execute("""CREATE TABLE IF NOT EXISTS people (
			id blob,
			coin real,
			bank real,
			bankmax real,
			server blob,
			inventory blob
			)""")
# commit
conn.commit()
# Create a table if does not exist people
c.execute("""CREATE TABLE IF NOT EXISTS organization (
			name blob,
			owner blob,
			cash real,
			people blob,
			inventory blob,
			mines blob
			)""")
# commit
conn.commit()

# shard id
shardids = 1
# shard count
shardcount = 1
# command prefix
commandprefix = ('s$','skyrona$', 'sky$', 'S$', 'Skyrona$', 'Sky$')
# cogs
path = f'F:/Skyrona/cogs'
cogs = []
for f in listdir(path):
	file = f"cogs.{f}".replace('.py', '')
	cogs += [file]
cogs.remove('cogs.__pycache__')
#cogs.remove('cogs.errorhandler')
print(cogs)


# get the bot started
bot = commands.AutoShardedBot(case_insensitive=True, loop=None, shard_id=shardids, shard_count=shardcount, command_prefix=commands.when_mentioned_or(*commandprefix))


statusofbot = open("F:/Skyrona/storage/status.txt", 'r')
statusbot = statusofbot.read().split('-')
statusofbot.close()
# sets the status of the game
if statusbot[1] == 'playing':
	game = discord.Activity(name=statusbot[0], type=discord.ActivityType.playing)
elif statusbot[1] == 'watching':
	game = discord.Activity(name=statusbot[0], type=discord.ActivityType.watching)
elif statusbot[1] == 'listening':
	game = discord.Activity(name=statusbot[0], type=discord.ActivityType.listening)

# when bot is ready
@bot.event
async def on_ready():
	# ... change the presence to game see var game for details
	await bot.change_presence(status=discord.Status.online, activity=game)

# loads the cogs
for extension in cogs:
	bot.load_extension(extension)

# run the bot
print("Running...")
x = datetime.datetime.now()
now = str(x.strftime("%d Day(s), %H Hour(s), %M Minute(s), %S Second(s)"))
f = open("F:/Skyrona/storage/started.txt", 'w')
f.write(now)
f.close()
bot.run(config)