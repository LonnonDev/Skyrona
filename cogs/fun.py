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

def printl(string):
	prn = open("C:/Users/Lemon/Desktop/Skyrona/output.txt", 'a')
	prn.write(f'\n{string}')
	prn.close()
	print(string)

# Connects to the database
conn = sqlite3.connect("people.db")
c = conn.cursor()

# Eco Cog
class Fun(commands.Cog, name="Fun Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def embedimg(self, ctx, img: str):
		color = random.randint(0, 0xFFFFFF)
		embed=discord.Embed(title=f"Image...", color=color)
		try:
			embed.set_image(url=img)
		except:
			# Silly random color
			color = random.randint(0, 0xFFFFFF)
			embed=discord.Embed(title=f"Invalid URL...", color=color)
			embed.set_author(name=str(ctx.author)[:-5],icon_url=ctx.author.avatar_url)
			embed.add_field(name="-", value=f"That's a invalid URL", inline=True)
			await ctx.send(embed=embed)
			return
		await ctx.send(embed=embed)

	@commands.command()
	async def minecraft(self, ctx):
		cancelled = False
		if cancelled:
			await ctx.send("Cancelled due to computing power requirements")
		else:
			await ctx.send("Minecraft server's ip is `67.82.206.23:25565` rn `Version: 20w12a (1.16 Snapshots)` **Snap shot Server**")

	@commands.command()
	@commands.is_owner()
	async def mathfunc(self, ctx,):
		embed=discord.Embed(title="Math", description="Math Functions Python")
		embed.add_field(name="ceil(x)", value="Returns the smallest integer greater than or equal to x.", inline=False)
		embed.add_field(name="copysign(x, y)", value="Returns x with the sign of y", inline=False)
		embed.add_field(name="fabs(x)", value="Returns the absolute value of x", inline=False)
		embed.add_field(name="factorial(x)", value="Returns the factorial of x", inline=False)
		embed.add_field(name="floor(x)", value="Returns the largest integer less than or equal to x", inline=False)
		embed.add_field(name="fmod(x, y)", value="Returns the remainder when x is divided by y", inline=False)
		embed.add_field(name="frexp(x)", value="Returns the mantissa and exponent of x as the pair (m, e)", inline=False)
		embed.add_field(name="fsum(iterable)", value="Returns an accurate floating point sum of values in the iterable", inline=False)
		embed.add_field(name="isfinite(x)", value="Returns True if x is neither an infinity nor a NaN (Not a Number)", inline=False)
		embed.add_field(name="isinf(x)", value="Returns True if x is a positive or negative infinity", inline=False)
		embed.add_field(name="isnan(x)", value="Returns True if x is a NaN", inline=False)
		embed.add_field(name="ldexp(x, i)", value="Returns x * (2**i)", inline=False)
		embed.add_field(name="modf(x)", value="Returns the fractional and integer parts of x", inline=False)
		embed.add_field(name="trunc(x)", value="Returns the truncated integer value of x", inline=False)
		embed.add_field(name="exp(x)", value="Returns e**x", inline=False)
		embed.add_field(name="expm1(x)", value="Returns e**x - 1", inline=False)
		embed.add_field(name="log(x[, base])", value="Returns the logarithm of x to the base (defaults to e)", inline=False)
		embed.add_field(name="log1p(x)", value="Returns the natural logarithm of 1+x", inline=False)
		embed.add_field(name="log2(x)", value="Returns the base-2 logarithm of x", inline=False)
		embed.add_field(name="log10(x", value="	Returns the base-10 logarithm of x", inline=False)
		embed.add_field(name="pow(x, y)", value="Returns x raised to the power y", inline=False)
		embed.add_field(name="sqrt(x)", value="Returns the square root of x", inline=False)
		embed.add_field(name="acos(x)", value="Returns the arc cosine of x", inline=False)
		embed.add_field(name="asin(x)", value="Returns the arc sine of x", inline=False)
		embed.add_field(name="atan(x)", value="Returns the arc tangent of x", inline=False)
		embed.add_field(name="atan2(y, x)", value="Returns atan(y / x)", inline=False)
		embed.add_field(name="cos(x)", value="Returns the cosine of x", inline=False)
		embed.add_field(name="hypot(x, y)", value="Returns the Euclidean norm, sqrt(x*x + y*y)", inline=False)
		embed.add_field(name="sin(x)", value="Returns the sine of x", inline=False)
		embed.add_field(name="tan(x)", value="Returns the tangent of x", inline=False)
		embed.add_field(name="degrees(x)", value="Converts angle x from radians to degrees", inline=False)
		embed.add_field(name="radians(x)", value="Converts angle x from degrees to radians", inline=False)
		embed.add_field(name="acosh(x)", value="Returns the inverse hyperbolic cosine of x", inline=False)
		embed.add_field(name="asinh(x)", value="Returns the inverse hyperbolic sine of x", inline=False)
		embed.add_field(name="atanh(x)", value="Returns the inverse hyperbolic tangent of x", inline=False)
		embed.add_field(name="cosh(x)", value="Returns the hyperbolic cosine of x", inline=False)
		embed.add_field(name="sinh(x)", value="Returns the hyperbolic cosine of x", inline=False)
		embed.add_field(name="tanh(x)", value="Returns the hyperbolic tangent of x", inline=False)
		embed.add_field(name="erf(x)", value="Returns the error function at x", inline=False)
		embed.add_field(name="erfc(x)", value="Returns the complementary error function at x", inline=False)
		embed.add_field(name="gamma(x)", value="Returns the Gamma function at x", inline=False)
		embed.add_field(name="lgamma(x)", value="Returns the natural logarithm of the absolute value of the Gamma function at x", inline=False)
		embed.add_field(name="pi", value="Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)", inline=False)
		embed.add_field(name="e", value="mathematical constant e (2.71828...)", inline=False)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.is_owner()
	async def math(self, ctx, *, math: str = '1 + 1'):
		async with ctx.typing():
			newmath = math.replace('^', '**')
			embed=discord.Embed(title="Math")
			embed.add_field(name="Problem", value=f"```diff\n{math}\n```", inline=False)
			embed.add_field(name="Answer", value=f"```diff\n{eval(newmath)}\n```", inline=False)
			await ctx.send(embed=embed)

	@commands.command()
	@commands.is_owner()
	async def solve(self, ctx, *, content: str = "1 + 1"):
		async with ctx.typing():
			content = f"$${content}$$"
			os.chdir('C:/Users/Lemon/Desktop/Skyrona/storage/')
			preview(r'{}'.format(content), viewer='file', filename='test.png', euler=False, dvioptions=["-D 6000"])
			os.chdir('C:/Users/Lemon/Desktop/Skyrona')
			await ctx.send('', file=discord.File(f'C:/Users/Lemon/Desktop/Skyrona/storage/test.png'))
			content = content.replace('$', '')
			slash = r'\\'
			content = str(content.replace('$', '').replace(slash, ''))
			solveit = eval(content)
			await ctx.send(content)
			await ctx.send(str(solveit))
			newmath = content.replace('^', '**')
			embed=discord.Embed(title="Math")
			embed.add_field(name="Problem", value=f"```diff\n{math}\n```", inline=False)
			embed.add_field(name="Answer", value=f"```diff\n{eval(newmath)}\n```", inline=False)
			await ctx.send(embed=embed)

	@commands.command()
	async def jönjlois(self, ctx, *, sentence: str = "Öe"):
		await ctx.send(sentence)
		setence = interpreter(sentence)
		await ctx.send(setence)

def interpreter(sentence):
	sentence = sentence.lower()
	# pronouns
	sentence = sentence.replace("öe", "I").replace("ou", "you").replace("õa", "he/she").replace("os", "we").replace("oua", "y'all").replace("oae", "they")
	# to be replacing
	## past
	sentence = sentence.replace("I opir", "I was").replace("you opir", "you were").replace("he/she opir", "he/she was").replace("we opir", "we were").replace("y'all opir", "y'all were").replace("they opir", "they were")
	## present
	sentence = sentence.replace("I oper", "I am").replace("you oper", "you are").replace("he/she oper", "he/she is").replace("we oper", "we are").replace("y'all oper", "y'all are").replace("they oper", "they are")
	## future
	sentence = sentence.replace("opar", "will")
	## Special
	sentence = sentence.replace("opler", "be")
	# verbs
	sentence = sentence.replace("dèq", "speak")
	# nouns
	sentence = sentence.replace("anjles", "English").replace("jönjlois", "Grak").replace("lajõ", "language")
	# adjectives
	sentence = sentence.replace("ènjlis", "English").replace("as", "epic")
	return sentence


def setup(bot):
	print("Fun Commands Loaded...")
	bot.add_cog(Fun(bot))
def teardown(bot):
	print("Fun Commands Unloaded...")