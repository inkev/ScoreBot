from discord.ext import commands

OWNER = 164582464050692096

def is_owner_check(message):
    return message.author.id == ID

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))