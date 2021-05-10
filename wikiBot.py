import wikipedia

def getWikiRandom():
    search = (wikipedia.random(pages=1))
    return getSearch(search)
def getWiki(message):
    search = message[6:] + "q"
    return getSearch(search)
def getSearch(search):
    try:
      x = wikipedia.summary(search)

      if len(x) > 2000:
          x = wikipedia.summary(search, sentences = 1)
      x = str(x.encode('ascii',errors='ignore'))

      x = x[1:]
      x = x.replace("\\n", " ")
      print(search)
      return(x)
      #await client.send_message(message.channel, x)
    except wikipedia.DisambiguationError as e:
        related_entries = str(e).split(":",1)[1].split("\n")[1:]
        reply = "This was too inspecific. Choose one from these:\n- {}".format("\n- ".join(related_entries))
        #await client.send_message(message.channel, reply)
        return(reply)
    except:
        print("---------------------------------------------")
        print(search)
        #print(x)
    #    await client.send_message(message.channel, "No results...")
        return ("No results, sorry :(")
