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
    "name": "",
    "insults": [
        "{name} ist sehr toll",
        "Jeder mag {name}. Warum auch nicht!?"
    ]
}
config_file = "config.json"

try:
    with open(config_file, "r") as f:
        config = json.load(f)
except IOError:
    with open(config_file, "w+") as f:
        json.dump(default_config, f, sort_keys=True, indent=4)
    sys.exit()

bot = commands.Bot(command_prefix=config["command_prefix"])

@bot.event
async def on_message(m):
    if m.author.id == config["scam_id"]:
        insult = random.choice(config["insults"])
        msg = insult.format(name=config["name"])
        await m.channel.send(msg)
        await m.delete()

bot.run(config["tokens"]["discord"])

