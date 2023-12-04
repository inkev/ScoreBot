from collections import namedtuple
import discord
from discord.ext import commands
import valo_api
import environment

HISTORY_VERSION = "v3"
REGION = "na"

player_dic = environment.PLAYER_DIC


class Valo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    valo_api.set_api_key(environment.VALOAPIKEY)

    @commands.hybrid_command()
    async def drink(self, ctx, name: str):
        player = player_dic[name]
        
        try:
            history = await valo_api.endpoints.get_match_history_by_name_async(HISTORY_VERSION, REGION, player.name, player.tag)
            team = self.check_team(player.name, history[0].players)
            drinks = self.calc_drinks(team, history)
            formatted = f"Your drink calculations are: \n{drinks}"
            print(formatted)
            await ctx.send(formatted)

        except Exception as e:
            await ctx.send("no match history you fucker")
            print(e)
        
    def check_team(self, name: str, players):
        for p in players.red:
            if name == p.name:
                return "red"
        return "blue"
    
    def calc_drinks(self, team, history):
        drinkString = ""
        drinks = 0
        rounds = history[0].rounds
        rnum = 0
        for r in rounds:
            rnum += 1
            for p_stats in r.player_stats:
                for kills in p_stats.kill_events:
                    if kills.damage_weapon_name is None and kills.killer_display_name != kills.victim_display_name:
                        drinkString += "{} knifed {} in round {}, that's a drink\n".format(kills.killer_display_name, kills.victim_display_name, rnum)
                        drinks += 1

        if not history[0].teams.to_dict()[team].has_won:
            drinkString += "You Lost +1\n"
            drinks += 1
            

        drinkString += "Drink Total = {}".format(drinks)
        return drinkString

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