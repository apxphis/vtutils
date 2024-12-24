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
    # ignore messages send by bot
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith("$ping"):
        await message.channel.send("Ping! ViaTech Utils here!")

    if msg.startswith("$commands"):
        await message.channel.send("""The commands available are:
                                   > $ping (test if the bot is awake)
                                   > $commands (view a list of commands)
                                   > $status (see player count and latencyping)
                                   > $statusfull (extended version of $status)""")

    status = server.status()
    if msg.startswith("$status"):
        await message.channel.send(f"The server has {status.players.online} players and replied in {status.latency} ms.")

    if msg.startswith("$statusfull"):
        query = server.query()
        await message.channel.send("The server has the following players online: {0}".format(", ".join(query.players.names)))

client.run(TOKEN)