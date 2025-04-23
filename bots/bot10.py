from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True 
intents.guilds = True
intents.members = True
token = os.getenv('DISCORD_BOT10_TOKEN')

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.send("hi")

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await vc.guild.me.edit()  # Server-mute the bot
    else:
        await ctx.send("You are not in a Voice channel") 

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

bot.run(token)