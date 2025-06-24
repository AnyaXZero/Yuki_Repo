from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app
from AnieXEricaMusic.mongo.afkdb import get_afk, set_afk, remove_afk
from AnieXEricaMusic.utils.mention import mention
import datetime

AFK_USERS = {}

# Command to set AFK
@app.on_message(filters.command("afk") & filters.me)
async def afk_command(_, message: Message):
    reason = message.text.split(None, 1)[1] if len(message.command) > 1 else "No reason provided"
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    await set_afk(user_id, reason)
    AFK_USERS[user_id] = datetime.datetime.utcnow()

    await message.reply_text(f" {mention(user_id, user_name)} is now AFK.\nReason: `{reason}`")

# Detect AFK user mentions and reply
@app.on_message(filters.group & filters.mentioned)
async def mention_afk(_, message: Message):
    if not message.entities:
        return

    for entity in message.entities:
        if entity.type == "mention" or entity.type == "text_mention":
            user = message.reply_to_message.from_user if message.reply_to_message else None
            if not user:
                continue

            afk_data = await get_afk(user.id)
            if afk_data:
                since = AFK_USERS.get(user.id, "a while ago")
                await message.reply_text(f" {mention(user.id, user.first_name)} is AFK.\nReason: `{afk_data['reason']}`")

# Remove AFK on user's first message back
@app.on_message(filters.text & filters.me)
async def remove_afk_status(_, message: Message):
    user_id = message.from_user.id
    afk_data = await get_afk(user_id)

    if afk_data:
        await remove_afk(user_id)
        AFK_USERS.pop(user_id, None)
        await message.reply_text(f" Welcome back, {mention(user_id, message.from_user.first_name)}! AFK status removed.")
