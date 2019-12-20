import discord
from discord.ext import commands
import random
import json

with open("config.json", "r") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=config["command_prefix"])

@bot.event
async def on_message(m):
    if m.author.id == config["scam_id"]:
        await m.channel.send(random.choice(config["insults"]))
        await m.delete()

bot.run(config["tokens"]["discord"])

