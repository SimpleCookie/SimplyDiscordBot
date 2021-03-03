import db
from datetime import datetime

dbPrefix = "heldt_runk_"

async def run(event):
  username = event.author.display_name
  #if event.content.startswith("!highscore"):
  highscore = db.listDBWithPrefix(dbPrefix)
  print(highscore)

  if db.keyExists(dbPrefix + username):
    oldRunk = db.getFromDB(dbPrefix, username)
    newRunk = increment(oldRunk)
    print("Updating to runk", newRunk)
    save(username, newRunk)
    await sendMsg(event, newRunk, username)  
  else:
    print("{} has no previous runks, creating ...".format(username))
    newRunk = create()
    save(username, newRunk)
    await sendMsg(event, newRunk, username)

def save(username, data):
  db.saveToDB(dbPrefix, username, data)

def create():
  return {
    "startdate": datetime.today().strftime('%Y-%m-%d'),
    "count": 1,
  }

async def sendMsg(event, data, username):
  timeMsg = "Runking for the {}:th time\n".format(str(data["count"]))
  textMsg = "Don't forget to sanitise your hands {}!\nKisses /Heldt!".format(username)
  fullText = "{}{}".format(timeMsg, textMsg)
  print(fullText)
  await event.channel.send(fullText)

def increment(data):
  return {
    "startdate": data["startdate"],
    "count": data["count"]+1
  }


    