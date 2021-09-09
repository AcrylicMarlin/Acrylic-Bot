from json import load
import discord
import os
from dotenv import load_dotenv
load_dotenv()


bot = discord.Client()

@bot.event
async def on_ready():
    print('Ready!')


bot.run(os.environ.get('TOKEN'))

