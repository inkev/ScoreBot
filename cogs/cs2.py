from demoparser2 import DemoParser
import discord
from discord.ext import commands

parser = DemoParser("path_to_demo.dem")
event_df = parser.parse_event("player_death", player=["X", "Y"], other=["total_rounds_played"])
ticks_df = parser.parse_ticks(["X", "Y"])

class Cs2(commands.cogs):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def cs_drink(self, ctx, name:str, dl:str):
        try:
            parser = DemoParser(dl)
            event_df = parser.parse_event()
            await ctx.send()
        
        except Exception as e:
            await ctx.send("no workie")
            print(e)

    @commands.hybrid_command()
    async def provide_demo(self, ctx, dl:str):
        try:
            await ctx.send("")
            
        except Exception as e:
            await ctx.send("no workie")
            print(e)