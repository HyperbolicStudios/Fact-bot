print("Go!")

import discord
from wikiBot import getWiki, getWikiRandom
from keep_alive import keep_alive
keep_alive()

TOKEN = "NTM0OTc1MjI0NDc1NjgwNzY4.D0S5kQ.2W7hOdDtsNL72q41jpd7zAo36tM"

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
#    await client.change_presence(game=discord.Game(name="Getting facts."))

@client.event #str(message.channel) != "botcommands"
async def on_message(message):
    if message.content == "!fact":
        channel = message.channel
        #print(getWikiRandom())
        await channel.send(getWikiRandom())
    elif message.content[:5] == "!fact":
        channel = message.channel
        await channel.send(getWiki(message.content))
    if message.content == "$fact_kill1":
        channel = message.channel
        channel.send("Loging out!")
        print("logout")
        await client.logout()
client.run(TOKEN)
