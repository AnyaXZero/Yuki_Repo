from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from AnieXEricaMusic import app

# Define your fonts (add more if needed)
def bold(text): return ''.join([chr(0x1D400 + ord(c) - 65) if 'A' <= c <= 'Z' else
                                chr(0x1D41A + ord(c) - 97) if 'a' <= c <= 'z' else c for c in text])
def italic(text): return ''.join(['𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡'.lower()[ord(c)-97]
                                  if 'a' <= c <= 'z' else '𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡'[ord(c)-65]
                                  if 'A' <= c <= 'Z' else c for c in text])
def mono(text): return ''.join(['𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣'[ord(c)-97]
                               if 'a' <= c <= 'z' else '𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉'[ord(c)-65]
                               if 'A' <= c <= 'Z' else c for c in text])

# Map style to function
style_map = {
    "bold": bold,
    "italic": italic,
    "mono": mono,
}

# Button layout
def font_keyboard():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("𝐁 Bold", callback_data="font_bold"),
             InlineKeyboardButton("𝘈 Italic", callback_data="font_italic")],
            [InlineKeyboardButton("𝙼 Mono", callback_data="font_mono"),
             InlineKeyboardButton("🅰️ a", callback_data="font_preview")],
        ]
    )

# Font command
@app.on_message(filters.command(["font", "fonts"]))
async def font_menu(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply("🔁 **Reply to a text message** to apply font style.")
    
    await message.reply(
        "**🎨 Choose a font style below:**",
        reply_markup=font_keyboard()
    )

# Font callback handler
@app.on_callback_query(filters.regex(r"^font_"))
async def font_callback(_, query: CallbackQuery):
    if not query.message.reply_to_message or not query.message.reply_to_message.text:
        return await query.answer("⚠️ Reply to a text message to style.", show_alert=True)

    original_text = query.message.reply_to_message.text
    action = query.data.split("_", 1)[1]

    if action == "preview":
        await query.answer("🅰️ Font preview button pressed.")
        return

    styler = style_map.get(action)
    if not styler:
        return await query.answer("🚫 Unknown font style.")

    styled_text = styler(original_text)

    try:
        await query.message.edit_text(
            styled_text,
            reply_markup=query.message.reply_markup
        )
    except Exception as e:
        print(f"[❌ ERROR APPLYING STYLE] {e}")
        await query.answer("❌ Failed to apply font style.")
