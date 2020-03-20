import time
import json
import random
import math
import discord
import os
import sys
import sqlite3
import secrets
import tex2pix
import datetime
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from sympy import preview
from sympy.solvers import solve
import asyncio
# Changes the directory
os.chdir('C:/Users/Lemon/Desktop/Skyrona')

# Connects to the database
conn = sqlite3.connect("people.db")
c = conn.cursor()

class beta(commands.Cog, name="Beta Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.is_owner()
	async def makemoneytest(self, ctx, amount: int):
		taxs = open("C:/Users/Lemon/Desktop/Skyrona/tax.txt", 'r')
		tax = taxs.read()
		addtax = (float(int(tax)) / 100) + 1
		removetax = float(int(tax)) / 100
		taxs.close()
		person = str(ctx.author.id)
		server = str(ctx.guild.id)
		c.execute("SELECT * FROM people WHERE id=? AND server=?", (person, server))
		# commit
		conn.commit()
		# fetch
		fetchall = c.fetchall()
		# user vars
		pocket = float(fetchall[0][1])

		earned = pocket + (amount - (amount * removetax))
		realearned = amount - (amount * removetax)
		taxearned = amount * removetax
		taxgive(taxearned, server)
		c.execute("UPDATE people SET coin=? WHERE id=? AND server=?", (earned, person, server))
		# commit
		conn.commit()
		color = random.randint(0, 0xFFFFFF)
		embed=discord.Embed(title="Earned...", color=color)
		embed.add_field(name="-", value=f"You got {realearned}\nYou payed {taxearned} in taxes", inline=False)
		embed.set_author(name=str(ctx.author)[:-5],icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.is_owner()
	async def leavethis(self, ctx):
		guild = ctx.guild
		await guild.leave()

def taxgive(give, server):
	if server == '636996896161923093':
		person = str(407313426751160353)
	elif server == '577072824355782656':
		person = str(670719216852140158)
	elif server == '680036875603542118':
		person = str(600798393459146784)
	c.execute("SELECT * FROM people WHERE id=? AND server=?", (person, server))
	# commit
	conn.commit()
	# fetch
	fetchall = c.fetchall()
	# user vars
	pocket = float(fetchall[0][1])

	earned = pocket + give

	c.execute("UPDATE people SET coin=? WHERE id=? AND server=?", (earned, person, server))
	# commit
	conn.commit()

# setup the Cog
def setup(bot):
	print("Beta Commands Loaded...")
	bot.add_cog(beta(bot))
def teardown(bot):
	print("Beta Commands Unloaded...")