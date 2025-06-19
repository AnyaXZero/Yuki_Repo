from pyrogram import filters, enums
from pyrogram.types import Message, ChatPermissions
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid, BadRequest
from datetime import timedelta
from AnieXEricaMusic.core.call import app

# Utility: mention function
def mention(user_id: int, name: str):
    return f"[{name}](tg://openmessage?user_id={user_id})"

# BAN Command
@app.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to ban.")
    
    user = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        await client.ban_chat_member(chat_id, user.id)
        await message.reply(
            f"{mention(user.id, user.first_name)} was **banned** by {mention(message.from_user.id, message.from_user.first_name)}.",
            quote=True
        )
    except ChatAdminRequired:
        await message.reply("❌ I need to be admin with ban rights.")
    except UserAdminInvalid:
        await message.reply("❌ Cannot ban another admin.")

# UNBAN Command
@app.on_message(filters.command("unban") & filters.group)
async def unban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to unban.")

    user = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        await client.unban_chat_member(chat_id, user.id)
        await message.reply(
            f"{mention(user.id, user.first_name)} was **unbanned** by {mention(message.from_user.id, message.from_user.first_name)}.",
            quote=True
        )
    except ChatAdminRequired:
        await message.reply("❌ I need to be admin with ban rights.")
    except BadRequest as e:
        await message.reply(f"Error: {e}")

# MUTE Command
@app.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to mute.")

    user = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        permissions = ChatPermissions(can_send_messages=False)
        await client.restrict_chat_member(chat_id, user.id, permissions=permissions)
        await message.reply(
            f"{mention(user.id, user.first_name)} was **muted** by {mention(message.from_user.id, message.from_user.first_name)}.",
            quote=True
        )
    except ChatAdminRequired:
        await message.reply("❌ I need to be admin with restrict rights.")
    except UserAdminInvalid:
        await message.reply("❌ Cannot mute another admin.")

# UNMUTE Command
@app.on_message(filters.command("unmute") & filters.group)
async def unmute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to unmute.")

    user = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True
        )
        await client.restrict_chat_member(chat_id, user.id, permissions=permissions)
        await message.reply(
            f"{mention(user.id, user.first_name)} was **unmuted** by {mention(message.from_user.id, message.from_user.first_name)}.",
            quote=True
        )
    except ChatAdminRequired:
        await message.reply("❌ I need to be admin with restrict rights.")
    except UserAdminInvalid:
        await message.reply("❌ Cannot unmute another admin.")
