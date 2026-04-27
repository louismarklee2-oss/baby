import discord
from discord import app_commands, ui
import asyncio
import random

TOKEN = 'token here'

BABY_WORDS = [
    "NIGGER", "NIGGER", "GET NIGGERED", "RAPE ", "KILL", "NIGGER", "FAGGOT", "NSDAP", 
    "island", "jungle", "kite", "lemon", "mountain", "night", "ocean", "piano",
    "queen", "rainbow", "sunset", "tiger", "umbrella", "violin", "waterfall", "xylophone",
    "yellow", "zebra", "angel", "baby", "cloud", "diamond", "eagle", "fire",
    "garden", "honey", "ice", "jewel", "king", "love", "moon", "star",
    "tree", "unicorn", "violet", "wolf", "box", "yacht", "zoo", "air",
    "book", "cat", "dog", "egg", "fish", "gold", "hat", "ink",
    "jar", "key", "lamp", "mouse", "nest", "orange", "pig", "quilt",
    "rose", "snake", "train", "unity", "voice", "wind", "fox", "yo-yo",
    "zip", "atom", "beam", "cube", "disk", "energy", "flame", "globe",
    "heart", "iris", "jade", "koala", "lotus", "mist", "nova", "opal",
    "pearl", "quartz", "ruby", "sage", "topaz", "aura", "bloom", "crimson",
    "dawn", "echo", "frost", "glade", "haven", "ivory", "jasmine", "karma",
    "lunar", "mystic", "nebula", "obsidian", "phoenix", "quiver", "ripple", "shadow",
    "thunder", "umbra", "valley", "whisper", "zenith", "azure", "bliss", "cascade",
    "drift", "ember", "fable", "glimmer", "harbor", "illusion", "journey", "kindle",
    "lagoon", "mirage", "nimbus", "oracle", "prism", "quest", "radiant", "solstice",
    "tide", "unity", "voyage", "wander", "yearn", "zephyr", "arctic", "breeze",
    "coral", "dusk", "eternal", "fjord", "gale", "horizon", "inferno", "jungle",
    "kelp", "lagoon", "meadow", "nature", "oasis", "plasma", "quartz", "reef",
    "savanna", "tundra", "utopia", "volcano", "willow", "xenon", "yonder", "zen",
    "acorn", "brook", "cliff", "dune", "estuary", "fern", "grove", "hill",
    "icicle", "jetty", "knoll", "lake", "marsh", "nook", "oak", "pond",
    "quarry", "ridge", "stream", "thicket", "undergrowth", "vale", "wood", "yew",
    "alley", "bridge", "canyon", "desert", "escarpment", "field", "glacier", "heath",
    "inlet", "juniper", "karst", "loch", "moor", "narrows", "outcrop", "prairie",
    "quagmire", "rainforest", "savannah", "taiga", "upland", "valley", "wetland", "xeric",
    "yardang", "zone", "amber", "bronze", "copper", "denim", "emerald", "fuchsia",
    "green", "hazel", "indigo", "jade", "khaki", "lime", "magenta", "navy",
    "olive", "pink", "quince", "red", "silver", "teal", "ultramarine", "vermilion",
    "white", "yellow", "aquamarine", "burgundy", "cerulean", "chartreuse", "cobalt", "damson",
    "ebony", "flax", "garnet", "heliotrope", "ivory", "jet", "kelly", "lavender",
    "maroon", "ochre", "periwinkle", "rose", "saffron", "taupe", "umber", "vanilla",
    "wheat", "zaffre", "alabaster", "beige", "carmine", "dandelion", "ecru", "fulvous"
]

IMAGE_LINKS = [
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253",
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253",
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253",
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253"
]

CUSTOM_LINKS = [
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253",
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253",
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253",
    "https://media.discordapp.net/attachments/1458707462592008274/1498437684996210779/download_3_-_Copy.png?ex=69f12857&is=69efd6d7&hm=2c7a2f14ce65547c5109b96cf7b0f1a7a6c88b522e044f11fe0e201351e2b5a8&=&format=webp&quality=lossless&width=253&height=253"
]

LINKS_PER_MESSAGE = 2

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.dm_messages = True

class BabyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.is_spamming = False
        self.target_channel_id = None

    async def setup_hook(self):
        await self.tree.sync()

bot = BabyBot()


class SayModal(ui.Modal, title="Enter your message"):
    user_input = ui.TextInput(
        label="Your message",
        placeholder="RAPE THIS SERVER NOW!!!...",
        required=True,
        max_length=1000
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        view = SayButtonView(self.user_input.value)
        await interaction.response.send_message(
            f"Click the button to spam 3 messages with: `{self.user_input.value}`",
            ephemeral=True,
            view=view
        )


class BabyCustomModal(ui.Modal, title="Enter your message"):
    user_input = ui.TextInput(
        label="Your message",
        placeholder="rape these niggers...",
        required=True,
        max_length=1000
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        view = BabyCustomButtonView(self.user_input.value)
        await interaction.response.send_message(
            "Click the button to rape the niggers!",
            ephemeral=True,
            view=view
        )


class BabyButtonView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.click_count = 0
    
    @ui.button(label="Start rape!", style=discord.ButtonStyle.green, custom_id="hitler_spam_button")
    async def start_spam_button(self, interaction: discord.Interaction, button: ui.Button):
        await interaction.response.defer(ephemeral=False)
        
        message_count = 10 if self.click_count == 0 else 3
        
        for i in range(message_count):
            try:
                random_words = " ".join(random.sample(NIGGER_WORDS, 10))
                msg = f"{random_words}\n\n" + "\n".join(IMAGE_LINKS)
                await interaction.followup.send(msg)
                if i < message_count - 1:
                    await asyncio.sleep(0.5)
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    await asyncio.sleep(e.retry_after if hasattr(e, 'retry_after') else 1)
                else:
                    break
            except Exception:
                break
        
        self.click_count += 1


class BabyCustomButtonView(ui.View):
    def __init__(self, custom_text):
        super().__init__(timeout=None)
        self.custom_text = custom_text

    @ui.button(label="Send Images", style=discord.ButtonStyle.blurple, custom_id="baby_custom_button")
    async def send_images_button(self, interaction: discord.Interaction, button: ui.Button):
        await interaction.response.defer(ephemeral=False)

        shuffled = CUSTOM_LINKS.copy()
        random.shuffle(shuffled)

        chunks = [shuffled[i:i+LINKS_PER_MESSAGE] for i in range(0, len(shuffled), LINKS_PER_MESSAGE)]

        for i, chunk in enumerate(chunks):
            try:
                msg = f"{self.custom_text}\n" + "\n".join(chunk)
                await interaction.followup.send(msg)
                if i < len(chunks) - 1:
                    await asyncio.sleep(0.5)
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    await asyncio.sleep(e.retry_after if hasattr(e, 'retry_after') else 1)
                else:
                    break
            except Exception:
                break


class SayButtonView(ui.View):
    def __init__(self, user_text):
        super().__init__(timeout=None)
        self.user_text = user_text
        self.click_count = 0
    
    @ui.button(label="Start RAPE", style=discord.ButtonStyle.green, custom_id="say_RAPE_button")
    async def start_spam_button(self, interaction: discord.Interaction, button: ui.Button):
        await interaction.response.defer(ephemeral=False)
        
        message_count = 10 if self.click_count == 0 else 3
        
        for i in range(message_count):
            try:
                await interaction.followup.send(self.user_text)
                if i < message_count - 1:
                    await asyncio.sleep(0.5)
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    await asyncio.sleep(e.retry_after if hasattr(e, 'retry_after') else 1)
                else:
                    break
            except Exception:
                break
        
        self.click_count += 1


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    print(f'{len(bot.guilds)} guilds')


@app_commands.command(name="natsocbot", description="HEIL HITLER!")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def baby_command(interaction: discord.Interaction):
    view = BabyButtonView()
    await interaction.response.send_message(
        "begin the RAPE",
        ephemeral=True,
        view=view
    )


@app_commands.command(name="hitlercustom", description="sike i lied nigger")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def babycustom_command(interaction: discord.Interaction):
    modal = BabyCustomModal()
    await interaction.response.send_modal(modal)


@app_commands.command(name="stop", description="it doesnt work nigger")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def stop_baby(interaction: discord.Interaction):
    if not bot.is_spamming:
        await interaction.response.send_message('nigger rape is not currently running.', ephemeral=True)
        return
    bot.is_spamming = False
    await interaction.response.send_message('stoppedcado')


@app_commands.command(name="ping these niggers", description="hitler status")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f'Pong! Latency: {latency}ms')


@app_commands.command(name="say2", description="qwahre")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def say2_command(interaction: discord.Interaction):
    modal = SayModal()
    await interaction.response.send_modal(modal)


bot.tree.add_command(baby_command)
bot.tree.add_command(babycustom_command)
bot.tree.add_command(stop_baby)
bot.tree.add_command(ping)
bot.tree.add_command(say2_command)

if __name__ == '__main__':
    bot.run(TOKEN)
