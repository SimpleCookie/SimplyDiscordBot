import discord
import os
import levelUp
import commands
import runk
import asyncio
from dotenv import dotenv_values
import logging


client = discord.Client()
config = dotenv_values(".env")

@client.event
async def on_ready():
  print("{0.user}.format(client) has signed in.")

@client.event
async def on_message(event):

  if event.author == client.user:
    return
    
  elif event.author == "MEE6":
    await handleMe6(event)

  elif event.content.startswith("Simply"):
    msgToSend = "Simply the best"
    await event.channel.send(msgToSend)
    print("Sent msg ", event.channel, "message:", msgToSend)

  elif event.content.startswith("!runk"):
      await runk.run(event)

  else:
    await commands.run(event)


async def handleMe6(event):
  await levelUp.handleLevelUp(event)

client.run(config.get("DISCORD_TOKEN"))