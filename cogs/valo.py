from collections import namedtuple
import discord
from discord.ext import commands
import valo_api

RiotId = namedtuple("RiotId", ("name", "tag"))
HISTORY_VERSION = "v1"
REGION = "na"

player_dic = {
    "inkev": RiotId("inkev", "NA1"),
    "Visate": RiotId("Visate", "OWO")
}


class Valo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def match(self, ctx, name: str):
        player = player_dic[name]
        
        try:
            history = await valo_api.endpoints.get_match_history_by_name_async(HISTORY_VERSION, REGION, player.name, player.tag)
            await ctx.send(history.players.red[0].name)
        except Exception as e:
            await ctx.send("no match history you fucker")
            print(e)

    @commands.hybrid_command()
    async def player(self, ctx, name: str):
        player = player_dic[name]

        try:
            account = await valo_api.endpoints.get_account_details_by_name_v1_async("v1", player.name, player.tag, True)
            await ctx.send(account.puuid)
        except Exception as e:
            await ctx.send("Can't find no bitch")
            print(e)
            



async def setup(bot):
    await bot.add_cog(Valo(bot))