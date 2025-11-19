from bot import bot

@bot.command()
async def test(ctx):
    await ctx.send("test")