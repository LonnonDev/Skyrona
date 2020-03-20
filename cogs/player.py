import time
import json
import random
import math
import discord
import os
import sys
import sqlite3
import secrets
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
# Changes the directory
os.chdir('F:/Skyrona')


# Connects to the database
conn = sqlite3.connect("people.db")
c = conn.cursor()

def printl(string):
	prn = open("F:/output.txt", 'a')
	prn.write(f'\n{string}')
	prn.close()
	print(string)

class player(commands.Cog, name="Shop/Inventory Commands"):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def shop(self, ctx, page: int = 1):
		await ctx.send('Mine (8,750) - 350 Ʀ per day')

	@commands.command()
	async def buy(self, ctx, item):
		item = item.lower()
		items = {'mine': '8750'}
		if item in items:
			person = str(ctx.author.id)
			server = str(ctx.guild.id)
			c.execute("SELECT * FROM people WHERE id=? AND server=?", (person, server))
			# commit
			conn.commit()
			# fetch
			fetchall = c.fetchall()
			name = fetchall[0][0]
			pocket = fetchall[0][1]
			mines = fetchall[0][6]
			if item == 'mine' and pocket >= int(items.get(item)):
				newmines = float(mines) + 1
				c.execute("UPDATE people SET mines=?, coin=? WHERE id=? AND server=?", (newmines, (float(pocket)-int(items.get(item))), person, server))
				conn.commit()
				await ctx.send("Bought it!")
			else:
				await ctx.send("You're a poor bitch")
		else:
			await ctx.send("Check `s$shop` for valid items")




def setup(bot):
	print("player Commands Loaded...")
	bot.add_cog(player(bot))
def teardown(bot):
	print("player Commands Unloaded...")