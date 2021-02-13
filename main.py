import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("{0.user}.format(client) has signed in.")

@client.event
async def on_message(event):
  if event.author == client.user:
    return
  if event.content.startswith("Simply"):
    msgToSend = "Simply the best"
    await event.channel.send(msgToSend)
    print("Sent msg ", event.channel, "message:", msgToSend)


client.run(os.getenv("DISCORD_TOKEN"))