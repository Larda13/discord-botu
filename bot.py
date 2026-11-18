import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif! Göreve hazır.")

@bot.event
async def on_member_join(member):
    mesaj = (
        f"Merhaba {member.name}! **{member.guild.name}** AİLEMİZE HOŞGELDİN🎉\n"
        f"Kuralları okumayı unutma, iyi eğlenceler!"
    )
    
    try:
        await member.send(mesaj)
        print(f"{member.name} adlı kişiye DM atıldı.")
    except discord.Forbidden:
        print(f"{member.name} adlı kişinin DM kutusu kapalı.")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)