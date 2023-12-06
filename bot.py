import discord
from discord.ext import commands
import cogs.utils.checks as checks
import environment

startup_extensions = ["cogs.valo", "cogs.cs2"]

description = "Hello, it's time"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", description = description, intents=intents, case_insensitive = True)

@bot.hybrid_command(hidden=True)
@checks.is_owner()
async def load(ctx, extension_name: str):
	# Loads an extension.
	try:
		await bot.load_extension("cogs.{}".format(extension_name))
	except (AttributeError, ImportError) as e:
		await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await ctx.send("{} loaded.".format(extension_name))


@bot.hybrid_command(hidden=True)
@checks.is_owner()
async def unload(ctx, extension_name: str):
	# Unloads an extension.
	await bot.unload_extension("cogs.{}".format(extension_name))
	await ctx.send("{} unloaded.".format(extension_name))


@bot.hybrid_command(hidden=True)
@checks.is_owner()
async def reload(ctx, extension_name:str):
	# Reloads an extension
	await bot.unload_extension("cogs.{}".format(extension_name))
	await ctx.send("{} unloaded.".format(extension_name))
	try:
		await bot.load_extension("cogs.{}".format(extension_name))
	except (AttributeError, ImportError) as e:
		await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await ctx.send("{} loaded.".format(extension_name))


@bot.hybrid_command(hidden=True)
@checks.is_owner()
async def synctree(ctx):
	await bot.tree.sync()
	await ctx.send("Command tree synced.")

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

    print("Synced slash commands for all users.")

bot.run(environment.TOKEN)