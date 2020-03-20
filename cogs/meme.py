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

# Eco Cog
class meme(commands.Cog, name="Meme Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def scienceteam(self, ctx):
		await ctx.send("https://www.youtube.com/watch?v=7S0dSDNdkK8")

	@commands.command()
	async def cheeto(self, ctx):
		await ctx.send("https://www.youtube.com/watch?v=XdI3NaaGAeo")

	# Tank Burger
	@commands.command(name="ТАНКОБУРГЕР")
	async def tankburger(self, ctx):
		await ctx.send('', file=discord.File(f'C:/Users/Lemon/Desktop/Skyrona/tankburger.jpg'))

	# Patchnot Command
	@commands.command(hidden=True)
	async def patchnots(self, ctx):
		await ctx.send("I GET IT IM RETARDED")

	@commands.command(name="Сука-блять", aliases=['Сукаблять'])
	async def cyka(self, ctx):
		await ctx.send("Сука блять\nhttps://www.youtube.com/watch?v=NqM032dnPtk")

def setup(bot):
	print("meme Commands Loaded...")
	bot.add_cog(meme(bot))
def teardown(bot):
	print("meme Commands Unloaded...")