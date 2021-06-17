import discord
from dicord.ext import commands

intents = discord.Intents.all()
bot = command.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Logged In As {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hey!")

bot.run("TOKEN")
