import discord
from discord.ext import commands
import random

insults = [
    'Simon ist schlimmer als Hitler',
    'Simon fickt furrys',
    'Simon ist ein Kanakken Negger',
    'Simon ist ein bildungsresistenter Intelligenzallergiker',
    'Simon, das einzige Positive in deinem Leben ist dein HIV Test',
    'Simon ist eine Gewitterziege',
    'Simon ist ein Wechselbalg',
    'Simon ist eine Gewitterziege',
    'Simon ist ein Wechselbalg'
]

bot = commands.Bot(command_prefix='$', description='Beleidigt Simon')

@bot.event
async def on_message(m):
    if m.author.id == 307909797699649536:
        await m.channel.send(random.choice(insults))
        await m.delete()

bot.run('MzcwNTU4MzU1NDE0MTg4MDMy.XfqdCg.M3KjK29WUfY-SKvVM2wi2kkf6pg')

