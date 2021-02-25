from replit import db

def addCommand(command, action):
  db["cmd_"+command] = action

def getCommand(command):
  cmd = db["cmd_"+command]
  return cmd

def listCommands():
  return db.prefix("cmd_")

async def handleAddCommand(event):
  if event.content.startswith("!addCommand "):
    split = event.content[12:].split(" ", 1)
    phrase = split[0]
    cmd = split[1]

    addCommand(phrase, cmd)
    await event.channel.send("Command "+ phrase +" has been registered")

async def handleCommandExec(event):
  cmd = getCommand(event.content[1:])
  if not cmd:
    print("Command doesn't exist", cmd)
    return
  print("Executing", cmd)
  await event.channel.send(cmd)

async def handleListCommands(event):
  cmds = listCommands()
  await event.channel.send(cmds)

def removeCommand(event):
  cmd = event.content.split(" ", 1)
  del db[cmd]

async def run(event):
  try:
    if event.content.startswith("!addCommand "):
      if event.author.display_name != "Devgroup.se":
        return
      await handleAddCommand(event)
    elif event.content.startswith("!list"):
      await handleListCommands(event)
    elif event.content.startswith("!remove"):
      if event.author.display_name != "Devgroup.se":
        return
      removeCommand(event)
    else:
      await handleCommandExec(event)
  except:
    print("Command doesn't exist", event.content)
