from pyrogram import Client, filters
from pyrogram.types import Message
from AnieXEricaMusic import app
from AnieXEricaMusic.mongo.karmadb import get_karma, update_karma

# Handle karma changes with +, ++, and -
@app.on_message(filters.text & filters.reply)
async def karma_plus_minus(client: Client, message: Message):
    text = message.text.strip()
    reply_user = message.reply_to_message.from_user
    from_user = message.from_user

    # Prevent self-karma
    if reply_user.id == from_user.id:
        return

    chat_id = message.chat.id
    user_id = reply_user.id

    if text == "+" or text == "++":
        await update_karma(chat_id, user_id, 1)
        await message.reply(f" Karma increased for {reply_user.mention}!")
    elif text == "-":
        await update_karma(chat_id, user_id, -1)
        await message.reply(f" Karma decreased for {reply_user.mention}!")

# Show karma value
@app.on_message(filters.command("karma"))
async def show_karma(client: Client, message: Message):
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    chat_id = message.chat.id
    user_id = user.id

    karma = await get_karma(chat_id, user_id)
    await message.reply(f"✨ Karma of {user.mention} is: `{karma}`")
