from interactions import Client, Intents, listen, slash_command, SlashContext
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Client(intents=Intents.DEFAULT)
@listen() 

async def on_ready():
    print(f"logged in as {bot.user}")

@slash_command(name="ping", description="you know what it does")
async def ping(ctx: SlashContext):
    await ctx.send("pong!")

@slash_command(name="support", description="join the support sever!")
async def support(ctx: SlashContext):
    await ctx.send("join our support server! https://discord.gg/JcBvUTVe7g")

bot.load_extension("exts.commands")

bot.start(TOKEN)