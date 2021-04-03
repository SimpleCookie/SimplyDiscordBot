import asyncio

async def handleLevelUp(event):
  msg = event.content
  levelSplit = msg.split(", you advanced to Level ")
  if len(levelSplit) == 2:
    userTarget = levelSplit[0][3:]
    nextLevel = levelSplit[1][:-1]
    if nextLevel == 3:
      await event.channel.send("Welcome to the game!" + userTarget)
      #await client.add_roles(userTarget, "Regular")
    if nextLevel == 10:
      await event.channel.send(userTarget + " is one of the cool kids now!")
      #await client.add_roles(userTarget, "Veteran")