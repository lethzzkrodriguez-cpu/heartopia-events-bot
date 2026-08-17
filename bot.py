import os
import threading
from flask import Flask
import discord
from discord.ext import commands

app = Flask(__name__)

@app.route("/")
def home():
    return "Heartopia Events Bot está online! 💜"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web).start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def teste(ctx):
    await ctx.send("🌷 Oii! Meu bot está funcionando! 💜")

@bot.command()
async def ajuda(ctx):
    await ctx.send(
        "🌷 **Heartopia Events** 💜\n\n"
        "✨ `!teste` — Testa se o bot está funcionando.\n"
        "📅 `!eventos` — Mostra os eventos disponíveis.\n"
        "🌸 `!ajuda` — Mostra este menu."
    )
@bot.command()
async def eventos(ctx):
    await ctx.send(
        "🌷 **Eventos do Heartopia** 💜\n\n"
        "🌠 Chuva de Meteoros — evento especial\n"
        "🎣 Evento de Pesca — fique de olho nos avisos!\n"
        "🎁 Eventos especiais — em breve!"
    )
@bot.command()
async def avisar(ctx, *, mensagem):
    await ctx.send(
        f"🔔 **AVISO DE HEARTOPIA** 🌷\n\n"
        f"{mensagem}\n\n"
        f"💜 Fiquem atentos aos eventos!"
    )
bot.run(os.getenv("DISCORD_TOKEN"))
