from bot import bot
from dotenv import load_dotenv
from os import getenv
import bot_events, bot_commands

load_dotenv()

bot.run(getenv("DISCORD_TOKEN"))