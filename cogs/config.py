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

class config(commands.Cog, name="Meta Commands"):
	def __init__(self, bot):
		self.bot = bot

	async def mod(ctx):
		# opens the modlist and then stores the data as a list
		modlist = open('C:/Users/Lemon/Desktop/Skyrona/storage/modlist.txt', 'r')
		modlist = modlist.read().split('-')
		# author's id
		authorid = str(ctx.author.id)
		# Check if the person is in the modlist
		if authorid in modlist:
			return True
		else:
			return False

	@commands.command()
	async def trello(self, ctx):
		await ctx.send("https://trello.com/b/PjeekMJV/skyrona-eco-bot")

	@commands.command()
	@commands.check(mod)
	async def settax(self, ctx, tax: str):
		if tax == 'on':
				tax = 10
		elif tax == 'off':
			tax = 0
		try:
			tax = int(tax)
		except:
			color = random.randint(0, 0xFFFFFF)
			embed=discord.Embed(title="Invalid Tax percentage", color=color)
			embed.add_field(name="-", value=f"```\nThat is not a number or an option```", inline=False)
			embed.set_author(name=str(ctx.author)[:-5],icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			return
		if tax > 100 or tax < 0:
			color = random.randint(0, 0xFFFFFF)
			embed=discord.Embed(title="Invalid Tax percentage", color=color)
			embed.add_field(name="-", value=f"```\n{tax} is not a valid amount to set the tax to```", inline=False)
			embed.set_author(name=str(ctx.author)[:-5],icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			return
		taxs = open("C:/Users/Lemon/Desktop/Skyrona/tax.txt", 'w')
		taxs.write(str(tax))
		taxs.close()
		taxpercent = str(tax) + "%"
		color = random.randint(0, 0xFFFFFF)
		embed=discord.Embed(title="Tax info", color=color)
		embed.add_field(name="Tax Percent", value=f"Tax is now {taxpercent}", inline=False)
		embed.set_author(name=str(ctx.author)[:-5],icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.check(mod)
	async def taxinfo(self, ctx):
		taxs = open("C:/Users/Lemon/Desktop/Skyrona/tax.txt", 'r')
		tax = taxs.read()
		taxs.close()
		taxpercent = str(int(tax) * 100) + "%"
		color = random.randint(0, 0xFFFFFF)
		embed=discord.Embed(title="Tax info", color=color)
		embed.add_field(name="Tax Percent", value=f"{taxpercent}", inline=False)
		embed.set_author(name=str(ctx.author)[:-5],icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)


# setup the Cog
def setup(bot):
	print("Configuration Commands Loaded...")
	bot.add_cog(config(bot))
def teardown(bot):
	print("Configuration Commands Unloaded...")