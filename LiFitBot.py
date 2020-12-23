# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix="<")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def waslos(ctx):
    while True:
        await ctx.send("@GoldNerd#5044")
        sleep(5)

client.run("NzgzMTE5NjUxNDcxMDk3ODg3.X8WHAg.RsLLrvPWGUt_ozfgBss2U8sAbkw")