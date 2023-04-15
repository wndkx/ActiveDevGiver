from discord import app_commands, Intents, Client, Interaction, Embed, Colour, SelectOption
import discord
import webbrowser
import jsony
import pyfiglet
import time

class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        await self.tree.sync()

client = Bot(intents=Intents.none())


@client.tree.command(name="getbadge", description="Gives you a badge")
async def give_badge(interaction: Interaction):
    main_embed = Embed(
        color=Colour.blue(),
        title="You got a badge",
        url="https://discord.com/developers/active-developer",
        description="Congrats! You got your Active Developer badge. To claim it click on the title and wait about 24 hours.  Here is more info that you must know:"
    )
    discord_devs = Embed(
        color=Colour.blue(),
        title="Discord Developers Server",
        url="https://discord.gg/discord-developers",
        description="Join to this server to know more information about badge"
    )
    issues = Embed(color=Colour.blue(), title="Issues",url="https://github.com", description="Sometimes the badge couldnt give correctly. To see all issues go to the ActiveDevGiver's github and go on Issues.")
    await interaction.response.send_message(embeds=[main_embed, discord_devs, issues])
if __name__ == "__main__":
    client_id = jsony.load_from_file("config.json")["client_id"]
    print(pyfiglet.figlet_format("ActiveDevGiver", "standard"))
    time.sleep(1.5)
    webbrowser.open(f"https://discord.com/api/oauth2/authorize?client_id={client_id}&permissions=2048&scope=bot")
    try:
        client.run(jsony.load_from_file("config.json")["token"])
    except discord.LoginFailure as err:
        print(f"ERR: {err}")