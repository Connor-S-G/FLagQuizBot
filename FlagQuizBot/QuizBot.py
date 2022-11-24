import random
import discord
from discord.ext import commands
import time

from CountrySelector import GetCountry

print(GetCountry())

TOKEN = "//YOUR KEY HERE//"

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print("Connected!")



@client.command()
async def play(ctx):
    img, name = GetCountry()
    await ctx.send(file=discord.File(img))
    string = "Click here to reveal answer: ||  "+name+"  ||"
    await ctx.send("Revealing in 3...")
    time.sleep(1)
    await ctx.send("2...")
    time.sleep(1)
    await ctx.send("1...")
    time.sleep(1)
    await ctx.send(string)

client.run(TOKEN)


