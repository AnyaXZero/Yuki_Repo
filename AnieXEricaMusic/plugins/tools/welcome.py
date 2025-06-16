from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from AnieXEricaMusic import app  # change to your bot's import if needed

# Welcome message
@app.on_message(filters.new_chat_members)
async def welcome(_, message: Message):
    for member in message.new_chat_members:
        await message.reply_photo(
            photo="https://files.catbox.moe/wvrrlg.jpg",
            caption=f"""───•❉᯽❉•───
❁ 𝐇𝐄𝐘 ━ {member.mention} •  
𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 {.chatname} ✨

➻ 𝐌𝐀𝐊𝐄 𝐍𝐄𝗪 𝐅𝐑𝐈𝐄𝐍𝐃𝐒 & 𝐒𝐓𝐀𝐘 𝐀𝐂𝐓𝐈𝐕𝐄 🌷✨
───•❉᯽❉•───""",
            reply_markup=InlineKeyboardMarkup(
                [
                  InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ", url="https://t.me/+C0s3qb7sRZA0ZjRk")
                    ],
                    [
                        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/YukiharaHiroto")
                    ]
                ]
            )
        )

# Goodbye message
@app.on_message(filters.left_chat_member)
async def goodbye(_, message: Message):
    left_member = message.left_chat_member
    await message.reply_text(
        f"""😢 {left_member.mention} ᴊᴜꜱᴛ ʟᴇꜰᴛ ᴛʜᴇ ɢʀᴏᴜᴩ...
ᴡᴇ'ʟʟ ᴍɪꜱꜱ ʏᴏᴜ 💔

❁ ꜱᴛᴀʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴡɪᴛʜ ᴜꜱ — {.chatname}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url="https://t.me/YukiMusiXbot")
                ]
            ]
        )
    )
