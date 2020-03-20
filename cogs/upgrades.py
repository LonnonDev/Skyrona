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
import discord.utils
# Changes the directory
os.chdir('F:/Skyrona')

# Connects to the database
conn = sqlite3.connect("people.db")
c = conn.cursor()

# upgrades cog
class upgrades(commands.Cog, name="Upgrading Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["bankupgrade", "ub"])
	async def upgradebank(self, ctx):
		# person using the command
		person = str(ctx.author.id)
		server = str(ctx.guild.id)
		# get them
		c.execute("SELECT * FROM people WHERE id=? AND server=?", (person, server))
		# commit
		conn.commit()
		# fetchall
		fetchall = c.fetchall()
		fetchall = fetchall[0]
		bank = float(fetchall[2])
		bankmax = float(fetchall[3])
		name = str(self.bot.get_user(int(person)))[:-5]
		if bank == bankmax:
			newbankmax = bankmax * 1.50
			newbankmax = float(newbankmax)
			c.execute("UPDATE people SET bank=0, bankmax=? WHERE id=? AND server=?", (newbankmax, person, server))
			conn.commit()
			embed=discord.Embed(title="Bank Upgraded!")
			embed.set_author(name=f"{name}",icon_url=ctx.author.avatar_url)
			embed.add_field(name="-", value=f"You upgraded you Bank you can now store, {newbankmax} Ʀ!", inline=False)
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="Not Enough...")
			embed.set_author(name=f"{name}",icon_url=ctx.author.avatar_url)
			embed.add_field(name="-", value="You don't have enough money for that", inline=False)
			await ctx.send(embed=embed)




def setup(bot):
	print("Upgrading Commands Loaded...")
	bot.add_cog(upgrades(bot))
def teardown(bot):
	print("Upgrading Commands Unloaded...")