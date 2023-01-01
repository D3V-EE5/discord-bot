from discord.ext import commands
import requests

# Current season API link:
# https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/171822096
# Past season API link:
# https://fantasy.espn.com/apis/v3/games/fba/leagueHistory/171822096?seasonId=<YEAR>
league_id = ""
c_url = "https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/"
p_url = "https://fantasy.espn.com/apis/v3/games/fba/leagueHistory/"

@commands.group()
async def fantasy(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("FILLER FOR INFO")

@fantasy.command()
async def register(ctx, league: str):
    if league.isnumeric():
        league_id = league
        c_url += league_id
        p_url = p_url + league_id + "?seasonId="
        
@fantasy.command()
async def pastMatchup(ctx, year: int):
    base = requests.get(p_url + str(year))
    r = requests.get("https://fantasy.espn.com/apis/v3/games/fba/leagueHistory/171822096?seasonId=2021&view=player_wl", params={"view": "player_wl"})
    await ctx.send(r.text[:1000])
    
async def setup(bot):
    league_id = "171822096"
    c_url = "https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/"
    p_url = "https://fantasy.espn.com/apis/v3/games/fba/leagueHistory/"
    bot.add_command(fantasy)
