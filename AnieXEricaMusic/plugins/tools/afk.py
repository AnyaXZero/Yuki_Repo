import os
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from AnieXEricaMusic import app
from AnieXEricaMusic.mongo.afkdb import set_afk, remove_afk, get_afk


@app.on_message(filters.command("afk") & filters.me)
async def afk_handler(_, message: Message):
    reason = " ".join(message.command[1:]) if len(message.command) > 1 else "ɪ'ᴍ ᴀꜰᴋ."

    await set_afk(message.from_user.id, reason)
    await message.reply_text(f"ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴀꜰᴋ!\n\n📝 ʀᴇᴀꜱᴏɴ: {reason}")


@app.on_message(filters.text & (filters.group | filters.private))
async def afk_check(_, message: Message):
    if not message.from_user:
        return

    sender_id = message.from_user.id

    # Remove AFK if user returns
    if await get_afk(sender_id):
        await remove_afk(sender_id)
        await message.reply_text("ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ! ʏᴏᴜ'ʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀꜰᴋ.")
        return

    # Reply if message mentions an AFK user
    if message.entities:
        mentioned_ids = []

        for ent in message.entities:
            if ent.type == "text_mention" and ent.user:
                mentioned_ids.append(ent.user.id)
            elif ent.type == "mention":
                username = message.text[ent.offset + 1 : ent.offset + ent.length]
                try:
                    user = await app.get_users(username)
                    mentioned_ids.append(user.id)
                except Exception:
                    continue

        for user_id in mentioned_ids:
            afk_data = await get_afk(user_id)
            if afk_data:
                reason = afk_data.get("reason", "AFK")
                since = afk_data.get("since")
                since_text = datetime.fromisoformat(since).strftime("%d %b %Y, %H:%M UTC") if since else "Unknown time"
                await message.reply_text(
                    f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ ᴀꜰᴋ!\n📝 ʀᴇᴀꜱᴏɴ: {reason}\n⏱️ Since: {since_text}"
                )
                break
