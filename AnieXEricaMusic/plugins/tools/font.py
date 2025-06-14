from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from AnieXEricaMusic import app
from font import Fonts

# Font style menu
@app.on_message(filters.command(["font", "fonts"]))
async def font_menu(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply("🔁 Reply to a text message to apply font style.")

    buttons = [
        [InlineKeyboardButton("𝗦𝗮𝗻𝘀", callback_data="style+sans"),
         InlineKeyboardButton("𝙎𝙖𝙣𝙨", callback_data="style+slant_sans"),
         InlineKeyboardButton("𝖲𝖺𝗇𝗌", callback_data="style+sim")],
        [InlineKeyboardButton("𝘚𝘢𝘯𝘴", callback_data="style+slant"),
         InlineKeyboardButton("𝐒𝐞𝐫𝐢𝐟", callback_data="style+serif"),
         InlineKeyboardButton("𝑺𝒆𝒓𝒊𝒇", callback_data="style+bold_cool")],
        [InlineKeyboardButton("𝓈𝒸𝓇𝒾𝓅𝓉", callback_data="style+script"),
         InlineKeyboardButton("𝓼𝓬𝓻𝓲𝓹𝓽", callback_data="style+script_bolt"),
         InlineKeyboardButton("𝑆𝑒𝑟𝑖𝑓", callback_data="style+cool")],
        [InlineKeyboardButton("sᴍᴀʟʟ cᴀᴘs", callback_data="style+small_cap"),
         InlineKeyboardButton("🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅨", callback_data="style+circle_dark"),
         InlineKeyboardButton("Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎", callback_data="style+circles")],
        [InlineKeyboardButton("𝕲𝖔𝖙𝖍𝖎𝖈", callback_data="style+gothic_bolt"),
         InlineKeyboardButton("𝔊𝔬𝔱𝔥𝔦𝔠", callback_data="style+gothic"),
         InlineKeyboardButton("ᵗⁱⁿʸ", callback_data="style+tiny")],
        [InlineKeyboardButton("𝕆𝕦𝕥𝕝𝕚𝕟𝕖", callback_data="style+outline"),
         InlineKeyboardButton("ᑕOᗰIᑕ", callback_data="style+comic"),
         InlineKeyboardButton("🇸 🇵 🇪 🇨 🇮 🇦 🇱 ", callback_data="style+special")],
        [InlineKeyboardButton("🅂🅀🅄🄰🅇🅴🅂", callback_data="style+squares"),
         InlineKeyboardButton("🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎", callback_data="style+squares_bold"),
         InlineKeyboardButton("ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ", callback_data="style+andalucia")],
        [InlineKeyboardButton("❌ Close", callback_data="close_reply")]
    ]

    await message.reply(
        "🎨 Choose a font style below:",
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

# Apply selected font style
@app.on_callback_query(filters.regex(r"^style\+"))
async def apply_style(_, query: CallbackQuery):
    _, style = query.data.split("+")

    if not query.message.reply_to_message or not query.message.reply_to_message.text:
        return await query.answer("⚠️ Replied text not found!", show_alert=True)

    original_text = query.message.reply_to_message.text.strip()

    # Available style mappings
    style_map = {
        "sans": Fonts.san,
        "slant_sans": Fonts.slant_san,
        "sim": Fonts.sim,
        "slant": Fonts.slant,
        "serif": Fonts.serief,
        "bold_cool": Fonts.bold_cool,
        "cool": Fonts.cool,
        "script": Fonts.script,
        "script_bolt": Fonts.bold_script,
        "small_cap": Fonts.smallcap,
        "circle_dark": Fonts.dark_circle,
        "circles": Fonts.circles,
        "gothic_bolt": Fonts.bold_gothic,
        "gothic": Fonts.gothic,
        "tiny": Fonts.tiny,
        "outline": Fonts.outline,
        "comic": Fonts.comic,
        "special": Fonts.special,
        "squares": Fonts.square,
        "squares_bold": Fonts.dark_square,
        "andalucia": Fonts.andalucia,
    }

    styler = style_map.get(style)
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
        await query.answer("❌ Failed to style text.")
styler = style_map.get(style)

if not styler:
    return await query.answer("🚫 Unknown font style.")

try:
    styled_text = styler(original_text)

    await query.message.edit_text(
        styled_text,
        reply_markup=query.message.reply_markup
    )

except Exception as e:
    print(f"[❌ ERROR APPLYING STYLE] {e}")
    await query.answer("❌ Failed to apply font style.")

# Optional: Handle close button
@app.on_callback_query(filters.regex("close_reply"))
async def close_reply(_, query: CallbackQuery):
    await query.message.delete()
