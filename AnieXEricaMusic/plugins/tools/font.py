from pyrogram import filters    
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery    
from AnieXEricaMusic import app    
    
# font.py

def typewriter(text):
    return ''.join([chr(0x1D68A + ord(c) - 97) if 'a' <= c <= 'z' else c for c in text.lower()])

def outline(text):
    outline_map = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅"
        "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
    )
    return text.translate(outline_map)

def serif(text):
    return ''.join([chr(0x1D434 + ord(c) - 65) if 'A' <= c <= 'Z'
                    else chr(0x1D44E + ord(c) - 97) if 'a' <= c <= 'z'
                    else c for c in text])

def smallcaps(text):
    return ''.join([chr(0x1D00 + ord(c.lower()) - 97) if 'a' <= c.lower() <= 'z' else c for c in text])

def script(text):
    return ''.join([chr(0x1D49C + ord(c) - 65) if 'A' <= c <= 'Z'
                    else chr(0x1D4B6 + ord(c) - 97) if 'a' <= c <= 'z'
                    else c for c in text])

def tiny(text):
    smalls = "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻ"
    return ''.join([smalls[ord(c) - 97] if 'a' <= c <= 'z' else c for c in text.lower()])

def comic(text):
    return text.upper()

def sans(text):
    return ''.join([chr(0x1D5A0 + ord(c) - 65) if 'A' <= c <= 'Z'
                    else chr(0x1D5BA + ord(c) - 97) if 'a' <= c <= 'z'
                    else c for c in text])

def odro(text):
    return 'ⓄⒹⓇⓄ ' + text

def circ(text):
    return ''.join(['ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ'[
        ord(c.lower()) - 97] if 'a' <= c.lower() <= 'z' else c for c in text])

def gothic(text):
    return ''.join([chr(0x1D56C + ord(c) - 65) if 'A' <= c <= 'Z'
                    else chr(0x1D586 + ord(c) - 97) if 'a' <= c <= 'z'
                    else c for c in text])

def clouds(text):
    return f'🌥️ {text} 🌥️'

def happy(text):
    return f'꒰⑅ᵕ༚ᵕ꒱˖♡ {text} ♡˖꒰ᵕ༚ᵕ⑅꒱'
            
FONT_STYLES = {
    "Typewri": typewriter,
    "Outline": outline,
    "Serif": serif,
    "SmallCa": smallcaps,
    "Script1": script,
    "Script2": script,
    "Tiny": tiny,
    "Comic": comic,
    "Sans1": sans,
    "Sans2": sans,
    "ODRO": odro,
    "CIRC": circ,
    "Gothic1": gothic,
    "Gothic2": gothic,
    "Clouds": clouds,
    "Happy": happy,
}

@app.on_message(filters.command("fonts"))
async def fonts_handler(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply("❗ Reply to a text to apply a font.")
    
    keyboard = [
        [InlineKeyboardButton(name, callback_data=f"font|{name}")]
        for name in list(FONT_STYLES.keys())
    ]
    await message.reply("🎨 Pick a font style:", reply_markup=InlineKeyboardMarkup(keyboard))

@app.on_callback_query(filters.regex("font\|"))
async def font_callback(client, callback_query: CallbackQuery):
    _, style = callback_query.data.split("|")
    func = FONT_STYLES.get(style)
    if not func:
        return await callback_query.answer("Invalid font.")

    original = callback_query.message.reply_to_message.text
    styled = func(original)

    await callback_query.message.edit_text(f"**{style} Style:**\n{styled}")

app.run()
