from bot import bot

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.lower() == 'ping':
        await message.channel.send('pong')