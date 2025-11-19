from bot import bot
from gift_roles import gift_roles_on_ready, gift_roles_on_raw_reaction_add, gift_roles_on_raw_reaction_remove

@bot.event
async def on_ready():
    print (f"Logged as {bot.user}")

    await gift_roles_on_ready()

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.lower() == 'ping':
        await message.channel.send('pong')

    if bot.user.mentioned_in(message):
        await message.add_reaction("❤️")

@bot.event
async def on_raw_reaction_add(payload):
    await gift_roles_on_raw_reaction_add(payload=payload)

@bot.event
async def on_raw_reaction_remove(payload):
    await gift_roles_on_raw_reaction_remove(payload=payload)