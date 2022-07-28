import requests
import disnake,os
from disnake.ext import commands
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="ez!",sync_commands_debug=True, intents=intents)
guild_id="17617271731222"
role_id="5272737284728294"
token = os.environ['token']#replit用
#token="OTkhsbausnwjssj90A"#一般
#
@bot.event
async def on_member_join(member):
  data=str(member.id)
  result =requests.put("https://discord.com/api/v9/guilds/{}/members/{}/roles/{}".format(guild_id, data, role_id), headers={"authorization":f"Bot {token}"})
  



bot.run(token)
