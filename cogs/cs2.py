from demoparser2 import DemoParser
import discord
from discord.ext import commands

class Cs2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def csdrink(self, ctx, name:str):
        try:
            parser = DemoParser("/home/inkev/demos/match.dem")
            df = parser.parse_event("player_hurt")

            he_dmg = he_kill(df)
            fire_dmg = df[(df["weapon"] == "molotov") | (df["weapon"] == "inferno")]

            print(fire_dmg)
            
            await ctx.send(he_dmg)
        
        except Exception as e:
            await ctx.send("no workie")
            print(e)

async def setup(bot):
    await bot.add_cog(Cs2(bot))

def he_kill(df):
    str = ""
    he_dmg = df[(df["weapon"] == "hegrenade") & (df["health"] == 0)]
    print(he_dmg)

    for k, d in zip(he_dmg.attacker_name, he_dmg.user_name):
        attacker = k
        take = d
        str += f"{attacker} killed {take} with a grenade\n"
    
    return str