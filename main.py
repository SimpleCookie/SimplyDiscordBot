import discord
import os
import levelUp
import commands

client = discord.Client()

@client.event
async def on_ready():
  print("{0.user}.format(client) has signed in.")

@client.event
async def on_message(event):
  if event.author == client.user:
    return
  await handleMe6(event)

  if event.content.startswith("Simply"):
    msgToSend = "Simply the best"
    await event.channel.send(msgToSend)
    print("Sent msg ", event.channel, "message:", msgToSend)

  await commands.run(event)

async def handleMe6(event):
  if event.author == "MEE6":
    await levelUp.handleLevelUp(event)


client.run(os.getenv("DISCORD_TOKEN"))