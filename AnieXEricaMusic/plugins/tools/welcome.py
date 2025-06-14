from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated

app = Client("my_bot")  # Replace with your actual app instance if different

WELCOME_TEXT = "ʜᴇʏ ᴡᴇʟᴄᴏᴍᴇ 🌷, {mention}!\nʜᴏᴩᴇ ʏᴏᴜ ᴇɴᴊᴏʏ ʜᴇʀᴇ!"
GOODBYE_TEXT = "👀 ɢᴏᴏᴅʙʏᴇ, {name}.\nᴡᴇ ʜᴏᴩᴇ ᴛᴏ ꜱᴇᴇ ʏᴏᴜ ᴀɢᴀɪɴ!"

# Welcome message on new member join
@app.on_chat_member_updated()
async def welcome_handler(client: Client, update: ChatMemberUpdated):
    if update.new_chat_member.status == "member" and update.old_chat_member.status != "member":
        mention = update.new_chat_member.user.mention
        text = WELCOME_TEXT.format(mention=mention)
        await app.send_message(chat_id=update.chat.id, text=text)

    elif update.new_chat_member.status in ["left", "kicked"]:
        name = update.new_chat_member.user.first_name
        text = GOODBYE_TEXT.format(name=name)
        await app.send_message(chat_id=update.chat.id, text=text)
