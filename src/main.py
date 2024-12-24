# dependencies
import discord
from dotenv import load_dotenv
import os
from mcstatus import JavaServer

load_dotenv()
TOKEN = os.getenv('TOKEN')
PUBLIC_IP = os.getenv('PUBLIC_IP')

# idk what this does tbh
intents = discord.Intents().all()
client = discord.Client(intents=intents)

# establish the server public IP
server = JavaServer.lookup(PUBLIC_IP)

# test if the bot can log in
@client.event
async def on_ready():
    print("log-in success ^-^")

# all the commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith("$ping"):
        await message.channel.send("Ping! ViaTech Utils here!")

    status = server.status()
    if msg.startswith("$status"):
        await message.channel.send(f"The server has {status.players.online} players and replied in {status.latency} ms.")

client.run(TOKEN)