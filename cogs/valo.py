from collections import namedtuple
import discord
from discord.ext import commands
import valo_api
import environment

RiotId = namedtuple("RiotId", ("name", "tag", "PUUID"))
HISTORY_VERSION = "v3"
REGION = "na"

player_dic = environment.PLAYER_DIC


class Valo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    valo_api.set_api_key(environment.VALOAPIKEY)

    @commands.hybrid_command()
    async def match(self, ctx, name: str):
        player = player_dic[name]
        
        try:
            history = await valo_api.endpoints.get_match_history_by_name_async(HISTORY_VERSION, REGION, player.name, player.tag)
            team = check_team(player.name, history[0].players)
            await ctx.send(team)

        except Exception as e:
            await ctx.send("no match history you fucker")
            print(e)
        
    def check_team(name: str, players):
        for p in players.red:
            if name == p.name:
                return "red"
        return "blue"



    @commands.hybrid_command()
    async def player(self, ctx, name: str):
        try:   
            player = player_dic[name]
            account = await valo_api.endpoints.get_account_details_by_name_async("v1", player.name, player.tag, True)
            await ctx.send(account.puuid)
        except Exception as e:
            await ctx.send("Can't find no bitch")
            print(e)
            



async def setup(bot):
    await bot.add_cog(Valo(bot))