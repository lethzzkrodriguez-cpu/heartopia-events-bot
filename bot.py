import os
import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def teste(ctx):
    await ctx.send("🌷 Oii! Meu bot está funcionando! 💜")

bot.run(os.getenv("DISCORD_TOKEN"))
