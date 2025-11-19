from bot import bot
from config import GIFT_ROLES_CHANNEL_ID, GIFT_ROLES_EMOJI

async def gift_roles_on_ready():
    channel = bot.get_channel(GIFT_ROLES_CHANNEL_ID)
    await channel.purge(limit=None)

    message = await channel.send("Рольки пустышки:")

    for emoji in GIFT_ROLES_EMOJI:
        await message.add_reaction(emoji)

async def gift_roles_on_raw_reaction_add(payload):
    if payload.channel_id == GIFT_ROLES_CHANNEL_ID:
        if payload.user_id == bot.user.id:
            return
        
        for emoji in GIFT_ROLES_EMOJI.keys():
            if str(payload.emoji) == emoji:
                guild = bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                role = guild.get_role(GIFT_ROLES_EMOJI[emoji])

                await member.add_roles(role)

async def gift_roles_on_raw_reaction_remove(payload):
    if payload.channel_id == GIFT_ROLES_CHANNEL_ID:
        if payload.user_id == bot.user.id:
            return
        
        for emoji in GIFT_ROLES_EMOJI.keys():
            if str(payload.emoji) == emoji:
                guild = bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                role = guild.get_role(GIFT_ROLES_EMOJI[emoji])

                await member.remove_roles(role)