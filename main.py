import discord
import os
from dotenv import load_dotenv
load_dotenv()


bot = discord.Bot()

@bot.event
async def on_ready():
    print(
'''{} is online
I am connected to {} servers.'''.format(bot.user.name, len(bot.guilds)))



@bot.slash_command(
    guild_ids=[859565691597226016],
    name = 'ping'
)
async def ping(ctx):
    await ctx.send('Pong {}ms'.format(round(bot.latency * 100, 0)))
































































































# Cogs aren't implemented, so this uneeded atm. Will re-add once implemented
# for cog in os.listdir('./cogs'):
#     if cog.endswith('.py') and not cog.startswith('_'):
#         try:
#             cog = f"cogs.{cog.replace('.py', '')}"
#             bot.load_extension(cog)
#         except Exception as e:
#             print(f"{cog} can not be loaded:")
#             raise e

























bot.run(os.environ.get('TOKEN'))

