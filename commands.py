import db
import runk

dbPrefix = "cmd_"

async def handleAddCommand(event):
  if event.content.startswith("!addCommand "):
    split = event.content[12:].split(" ", 1)
    phrase = split[0]
    cmd = split[1]
    if phrase[0] != "!":
      await event.channel.send("Missing [!phrase]")
      return

    db.saveToDB(dbPrefix, phrase[1:], cmd)
    await event.channel.send("Command "+ phrase +" has been registered")

async def handleCommandExec(event):
  cmd = db.getFromDB(dbPrefix, event.content[1:])
  if not cmd:
    print("Command doesn't exist:", cmd)
    return
  print("Executing", cmd)
  await event.channel.send(cmd)

async def handleListCommands(event):
  cmds = db.listDBWithPrefix()
  await event.channel.send(cmds)

def removeCommand(event):
  cmd = event.content.split(" ", 1)
  db.removeCommand(dbPrefix, cmd)

async def run(event):
  try:
    if event.content.startswith("!addCommand "):
      if event.author.display_name != "Devgroup.se":
        return
      await handleAddCommand(event)
    elif event.content.startswith("!list"):
      await handleListCommands(event)
      return
    elif event.content.startswith("!remove"):
      if event.author.display_name != "Devgroup.se":
        return
      removeCommand(event)
    else:
      await handleCommandExec(event)
  except:
    print("Command doesn't exist", event.content)
