import client
from dotenv import load_dotenv
from os import getenv
from src.core.logging.init_logs import log_handler
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

load_dotenv()

client = client.Bot()
client.run(getenv("DISCORD_TOKEN"), log_handler=log_handler)
