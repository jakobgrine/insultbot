import discord
from discord.ext import commands
import random
import json
import sys

default_config = {
    "scam_id": "",
    "command_prefix": "",
    "tokens": {
        "discord": "",
    },
    "insults": []
}

try:
    with open("config.json", "r") as f:
        config = json.load(f)
except IOError:
    with open("config.json", "w+") as f:
        json.dump(default_config, f, sort_keys=True, indent=4)
    sys.exit()

bot = commands.Bot(command_prefix=config["command_prefix"])

@bot.event
async def on_message(m):
    if m.author.id == config["scam_id"]:
        await m.channel.send(random.choice(config["insults"]))
        await m.delete()

bot.run(config["tokens"]["discord"])

