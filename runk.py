from db import db
import asyncio
from datetime import datetime


async def run(event):
  username = event.author.display_name
  #if event.content.startswith("!highscore"):
  highscore = db.getRunkHighscore()
  print(highscore)

  result = db.addRunk(username)
  print("Runks", result)
  await sendMsg(event, result, username)  

async def sendMsg(event, data, username):
  timeMsg = "Runking for the {}:th time\n".format(str(data["count"]))
  textMsg = "Don't forget to sanitise your hands {}!\nKisses /Heldt!".format(username)
  fullText = "{}{}".format(timeMsg, textMsg)
  print(fullText)
  await event.channel.send(fullText)

    