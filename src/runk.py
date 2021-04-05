from database import db
import asyncio
from datetime import datetime


async def run(event):
  username = event.author.display_name
  db.addRunk(username)
  score = db.getRunkHighscoreByUsername(username)
  await sendRunkMsg(event, score, username)  

async def highscore(event):
  highscore = db.getRunkHighscore()
  await event.channel.send(highscore)


async def sendRunkMsg(event, data, username):
  timeMsg = "Runking for the {}:th time\n".format(str(data.get("score")))
  textMsg = "Don't forget to sanitise your hands {}!\nKisses /Heldt!".format(username)
  fullText = "{}{}".format(timeMsg, textMsg)
  await event.channel.send(fullText)


    