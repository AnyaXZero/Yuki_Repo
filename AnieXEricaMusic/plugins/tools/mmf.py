import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app
from font import get_font
from tempfile import mktemp

SUPPORTED_MIME = ["image/", "video/mp4", "image/webp", "application/x-tgsticker"]

@app.on_message(filters.command("mmf"))
async def mmf(_, message: Message):
    reply = message.reply_to_message
    if not reply or not (reply.photo or reply.sticker or reply.document):
        return await message.reply_text("📸 Reply to an image, sticker, or GIF to meme it!")

    if len(message.text.split()) < 2:
        return await message.reply_text("💬 Provide text like:\n`/mmf Top Text;Bottom Text`")

    msg = await message.reply_text("❄️ Creating your meme...")
    text = message.text.split(None, 1)[1]

    # Download media
    media = await app.download_media(reply, file_name=mktemp(suffix=".tmp"))
    if reply.sticker and reply.sticker.is_animated:
        await msg.edit("⚠️ Animated stickers (.TGS) are not yet supported for text overlay.")
        os.remove(media)
        return

    meme = await draw_text(media, text)
    if meme.endswith(".webp") or meme.endswith(".jpg"):
        await message.reply_photo(photo=meme)
    else:
        await message.reply_document(document=meme)

    await msg.delete()
    os.remove(meme)


async def draw_text(image_path, text: str) -> str:
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception:
        return "❌ Couldn't open the image."
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

    width, height = img.size
    font = get_font(size=int(width / 15))  # Adjust font size based on width
    draw = ImageDraw.Draw(img)

    top_text, bottom_text = (text.split(";", 1) + [""])[:2]
    wrap_width = max(20, width // 40)

    def outline(draw, x, y, text, font):
        # Draw black outline
        for dx, dy in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            draw.text((x + dx, y + dy), text, font=font, fill="black")
        draw.text((x, y), text, font=font, fill="white")

    # Draw top text
    if top_text:
        current_h = 10
        for line in textwrap.wrap(top_text, width=wrap_width):
            bbox = font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (width - text_width) / 2
            outline(draw, x, current_h, line, font)
            current_h += text_height + 5

    # Draw bottom text
    if bottom_text:
        lines = textwrap.wrap(bottom_text, width=wrap_width)
        total_height = sum(font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines) + 5 * len(lines)
        current_h = height - total_height - 10
        for line in lines:
            bbox = font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (width - text_width) / 2
            outline(draw, x, current_h, line, font)
            current_h += text_height + 5

    output_file = f"memify_{os.urandom(4).hex()}.webp"
    img.save(output_file, "webp")
    return output_file
