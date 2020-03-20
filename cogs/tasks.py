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
from discord.ext import tasks
import asyncio
import discord.utils
os.chdir('F:/Skyrona')

# Connects to the database
conn = sqlite3.connect("people.db")
c = conn.cursor()

def printl(string):
	prn = open("F:/Skyrona/output.txt", 'a')
	prn.write(f'\n{string}')
	prn.close()
	print(string)

# task cog
class tasks(commands.Cog, name="tasks"):
	def __init__(self, bot):
		self.bot = bot
		self.mines.start()
		self.checkbank.start()
		#self.changeowl.start()
		self.plagueinc.start()
		self.paygov.start()

	def cog_unload(self):
		self.plagueinc.cancel()
		self.checkbank.stop()

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.channel.id == 684187458052685847:
			await message.add_reaction('❤️')
			await message.add_reaction('💔')

	@tasks.loop(seconds=1.0, reconnect=True)
	async def changeowl(self):
		nickname = "Retard87"
		await self.bot.wait_until_ready()
		guild = self.bot.get_guild(636996896161923093)
		member = guild.get_member(534780073358655493)
		await member.edit(nick=nickname)

	# this task is for bank interest
	@tasks.loop(hours=24.0, reconnect=True)
	async def mines(self):
		# select from people5
		c.execute("SELECT * FROM people WHERE NOT mines=0")
		# commit
		conn.commit()
		# fetch
		fetchall = c.fetchall()
		fetchlength = len(fetchall)
		x = 0
		for x in range(fetchlength):
			name = str(fetchall[x][0])
			server = str(fetchall[x][4])
			pocket = float(fetchall[x][1])
			newbal = float(pocket) + (float(pocket) + 100)
			# Update their money
			c.execute("UPDATE people SET coin=? WHERE id=? AND server=?", (newbal, name, server))
			# commit
			conn.commit()
			x += 1 

	@tasks.loop(seconds=1.0, reconnect=True)
	async def checkbank(self):
		# select from people5
		c.execute("SELECT * FROM people")
		# commit
		conn.commit()
		# fetch
		fetchall = c.fetchall()
		fetchlength = len(fetchall)
		for x in range(len(fetchlength)):
			name = str(fetchall[x][0])
			server = str(fetchall[x][4])
			pocket = round(float(fetchall[x][1]), 2)
			bank = round(float(fetchall[x][2]), 2)
			bankmax = round(float(fetchall[x][3]), 2)
			c.execute("UPDATE people SET coin=?, bank=? WHERE id=? AND server=?", (newbank, bankmax, name, server))
			# commit
			conn.commit()

	@tasks.loop(hours=24.0, reconnect=True)
	async def paygov(self):
		employees = ['319663383538565120', '444681618758696980', '673508525607092236', '600798393459146784', '251921855521226753', '327535067675099148', '404561073715281931', '616988819052560405', '360225671382958081']
		for x in range(len(employees)):
			c.execute("SELECT * FROM people WHERE id=? AND server=?", (str(employees[x]), '636996896161923093'))
			# commit
			conn.commit()
			# fetch
			fetchall = c.fetchall()
			pocket = round(float(fetchall[0][1]), 2)
			newpocket = pocket + 350
			c.execute("UPDATE people SET coin=? WHERE id=? AND server=?", (newpocket, str(employees[x]), "636996896161923093"))
			# commit
			conn.commit()


	@tasks.loop(seconds=1.0, reconnect=True)
	async def checkbank(self):
		# select from people5
		c.execute("SELECT * FROM people WHERE NOT bank=0")
		# commit
		conn.commit()
		# fetch
		fetchall = c.fetchall()
		fetchlength = len(fetchall)
		x = 0
		for x in range(fetchlength):
			name = str(fetchall[x][0])
			pocket = float(fetchall[x][1])
			bank = float(fetchall[x][2])
			bankmax = fetchall[x][3]
			if bankmax == "∞":
				bankmax = float('inf')
			else:
				bankmax = float(bankmax)
			if bank > bankmax:
				newbank = (bank - bankmax) + pocket
				# Update their money
				c.execute("UPDATE people SET coin=?, bank=? WHERE id=? AND server=?", (newbank, bankmax, name))
				# commit
				conn.commit()
			x += 1

	@tasks.loop(seconds=120, reconnect=True)
	async def plagueinc(self):
		plague = """
We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching but you're too shy to say it Inside we both know what's been going on We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give, never gonna give (Give you up) (Ooh) Never gonna give, never gonna give (Give you up) We've known each other for so long Your heart's been aching but you're too shy to say it Inside we both know what's been going on We know the game and we're gonna play it I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry"""
		plague = plague.split(' ')
		await self.bot.wait_until_ready()
		gu = self.bot.get_guild(636996896161923093)
		guildmeber = gu.get_member(683737063434354725)
		plaguelength = len(plague)
		number = 0
		while True:
			await guildmeber.edit(nick=f"! {str(plague[number])}", reason="Flame Gang")
			await asyncio.sleep(0.1)
			if plaguelength == number:
				number = 0
			else:
				number += 1
		"""async for member in gu.members:
									print(person.name)
									await person.edit(nick="Flame")
									await asyncio.sleep(5)"""
			
def setup(bot):
	print("Tasks Commands Loaded")
	bot.add_cog(tasks(bot))
def teardown(bot):
	print("Tasks Commands Unloaded...")