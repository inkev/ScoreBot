import discord
from discord.ext import commands
import cogs.utils.checks as checks
import environment

startup_extensions = ["cogs.valo"]

description = "fuck you"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", description = description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as \n{bot.user}\n{bot.user.id}")
    
    for extension in startup_extensions:
        try:
            await bot.load_extension(extension)
            print(f"Loaded {extension}")
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    await bot.tree.sync()
    print("Synced slash commands for all users.")

bot.run(environment.TOKEN)