from pyrogram import filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid
from AnieXEricaMusic import app  # Replace with your actual client import

def mention(user_id, name):
    return f"[{name}](tg://user?id={user_id})"

@app.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to ban them.")
    try:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply(f"{mention(user_id, user_name)} has been banned.")
    except ChatAdminRequired:
        await message.reply("I need to be an admin with ban rights.")
    except UserAdminInvalid:
        await message.reply("I can't ban an admin.")

@app.on_message(filters.command("unban") & filters.group)
async def unban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to unban them.")
    try:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply(f"{mention(user_id, user_name)} has been unbanned.")
    except ChatAdminRequired:
        await message.reply("I need to be an admin with unban rights.")

@app.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to mute them.")
    try:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        permissions = ChatPermissions(can_send_messages=False)
        await client.restrict_chat_member(message.chat.id, user_id, permissions=permissions)
        await message.reply(f"{mention(user_id, user_name)} has been muted.")
    except ChatAdminRequired:
        await message.reply("I need to be an admin with mute rights.")

@app.on_message(filters.command("unmute") & filters.group)
async def unmute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to unmute them.")
    try:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True
        )
        await client.restrict_chat_member(message.chat.id, user_id, permissions=permissions)
        await message.reply(f"{mention(user_id, user_name)} has been unmuted.")
    except ChatAdminRequired:
        await message.reply("I need to be an admin with unmute rights.")
