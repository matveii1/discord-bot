from bot import bot

@bot.command()
async def hi(ctx):
    await ctx.send("lol")