print("Go!")

import discord
import wikipedia

TOKEN = "NTM0OTc1MjI0NDc1NjgwNzY4.D0S5kQ.2W7hOdDtsNL72q41jpd7zAo36tM"

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Getting facts."))

@client.event #str(message.channel) != "botcommands"
async def on_message(message):
    if message.author == client.user or (str(message.content))[:5] != "!fact":
        print("Message blocked: " + str(message.content)[:5])
        return
    else:
        if len(str(message.content)) == 5:
            search = (wikipedia.random(pages=1))
        else:
            search = (str(message.content))[5:]
        try:
          x = wikipedia.summary(search)

          if len(x) > 2000:
              x = wikipedia.summary(search, sentences = 1)
          x = str(x.encode('ascii',errors='ignore'))

          x = x[1:]
          x = x.replace("\\n", " ")

          await client.send_message(message.channel, x)
        except wikipedia.DisambiguationError as e:
            related_entries = str(e).split(":",1)[1].split("\n")[1:]
            reply = "This was too inspecific. Choose one from these:\n- {}".format("\n- ".join(related_entries))
            await client.send_message(message.channel, reply)
        except:
            print("---------------------------------------------")
            print(search)
            print(x)
            await client.send_message(message.channel, "No results...")
client.run(TOKEN)
