from interactions import Extension, slash_command, SlashContext, OptionType, slash_option
from mcstatus import JavaServer
from mojang import Client
from mojang import API

api = API()

class ViaTechCommands(Extension):
    @slash_command(name="status", description="checks the status of a given server ip.")
    @slash_option(
        name="server_ip",
        description="give the server you'd like to search",
        required=True,
        opt_type=OptionType.STRING
    )

    async def check_status(self, ctx: SlashContext, server_ip: str):
        try:
            server = JavaServer.lookup(server_ip)
            status = server.status()
            await ctx.send(f"{server_ip} currently has {status.players.online} players online and responded in {status.latency} ms")
        except Exception as e:
            print(f"{e}")

    @slash_command(name="playerinfo", description="get some player info!")
    @slash_option(
        name="username",
        description="give the username to get the info",
        required=True,
        opt_type=OptionType.STRING
    )
    async def playerinfo(self, ctx: SlashContext, username: str):
        uuid = api.get_uuid(username)
        profile = api.get_profile(uuid)
        if not uuid:
            await ctx.send(f"{username} is not taken!")
        else:
            await ctx.send(f"{username} is currently wearing the {profile.skin_url} and is using the {profile.skin_variant} variant")

    @slash_command(name="low", description="go ahead, see what it does")
    async def taper_fade(self, ctx: SlashContext):
        await ctx.send("LOOOOOOOOOW TAPER FAAAAADE")
    