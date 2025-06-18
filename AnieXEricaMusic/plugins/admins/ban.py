import logging
import re
import datetime
from pyrogram import filters, enums
from pyrogram.types import ChatPermissions
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid

from AnieXEricaMusic.core.call import app

# Configure logging
logging.basicConfig(
    filename='moderation.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def mention(user_id, name, mention=True):
    """Create a Telegram user mention."""
    if mention:
        return f"[{name}](tg://openmessage?user_id={user_id})"
    return f"[{name}](https://t.me/{user_id})"

async def get_userid_from_username(username):
    """Retrieve user ID and first name from username."""
    try:
        user = await app.get_users(username)
        return [user.id, user.first_name]
    except:
        return None

def parse_duration(time_str):
    """Parse time duration (e.g., 2m, 3h, 1d)."""
    match = re.match(r'^(\d+)([mhd])$', time_str.strip())
    if not match:
        return None
    amount, unit = int(match.group(1)), match.group(2)
    if amount <= 0 or amount > 365:  # Prevent excessive durations
        return None
    if unit == 'm':
        return datetime.timedelta(minutes=amount)
    elif unit == 'h':
        return datetime.timedelta(hours=amount)
    elif unit == 'd':
        return datetime.timedelta(days=amount)

async def extract_user(message):
    """Extract user ID, first name, and reason/time from message."""
    reason = None
    time_str = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        if len(message.command) > 1:
            reason = message.text.split(None, 1)[1].strip()
            time_str = reason if message.command[0] == 'tmute' else None
    elif len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except ValueError:
            user_obj = await get_userid_from_username(message.command[1])
            if not user_obj:
                return None, None, None
            user_id, first_name = user_obj
        if len(message.text.split()) > 2:
            args = message.text.partition(message.command[1])[2].strip()
            reason = args if message.command[0] != 'tmute' else None
            time_str = args if message.command[0] == 'tmute' else None
    else:
        return None, None, None
    return user_id, first_name, reason, time_str

async def check_admin_permissions(message, admin_id):
    """Check if the user is an admin with restrict permissions."""
    member = await message.chat.get_member(admin_id)
    if member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        return False, "You don't have permission to perform this action."
    if not member.privileges.can_restrict_members:
        return False, "You lack the necessary permissions to restrict members."
    return True, None

async def ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason=None, time=None):
    """Ban a user from the chat."""
    msg_text = ""
    bot_id = (await app.get_me()).id
    try:
        if user_id == bot_id:
            msg_text = "Why should I ban myself? I'm not that silly!"
            return msg_text, False
        await app.ban_chat_member(chat_id, user_id)
        logging.info(f"Ban: User {user_id} ({first_name}) banned by {admin_id} ({admin_name}) in chat {chat_id}. Reason: {reason or 'None'}")
    except ChatAdminRequired:
        msg_text = "I need ban rights to perform this action! 😡🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I won't ban an admin!"
        return msg_text, False
    except Exception as e:
        msg_text = f"Oops! Something went wrong: {e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    msg_text = f"{user_mention} was banned by {admin_mention}\n"
    if reason:
        msg_text += f"Reason: `{reason}`\n"
    if time:
        msg_text += f"Time: `{time}`\n"
    return msg_text, True

async def unban_user(user_id, first_name, admin_id, admin_name, chat_id):
    """Unban a user from the chat."""
    msg_text = ""
    try:
        await app.unban_chat_member(chat_id, user_id)
        logging.info(f"Unban: User {user_id} ({first_name}) unbanned by {admin_id} ({admin_name}) in chat {chat_id}.")
    except ChatAdminRequired:
        msg_text = "I need ban rights to perform this action! 😡🥺"
        return msg_text
    except Exception as e:
        msg_text = f"Oops! Something went wrong: {e}"
        return msg_text

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    msg_text = f"{user_mention} was unbanned by {admin_mention}"
    return msg_text

async def mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason=None, time=None):
    """Mute a user in the chat."""
    msg_text = ""
    bot_id = (await app.get_me()).id
    try:
        if user_id == bot_id:
            msg_text = "Why should I mute myself? I'm not that silly!"
            return msg_text, False
        if time:
            mute_end_time = datetime.datetime.now() + time
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), mute_end_time)
        else:
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions())
        logging.info(f"Mute: User {user_id} ({first_name}) muted by {admin_id} ({admin_name}) in chat {chat_id}. Reason: {reason or 'None'}, Duration: {time or 'Permanent'}")
    except ChatAdminRequired:
        msg_text = "I need mute rights to perform this action! 😡🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I won't mute an admin!"
        return msg_text, False
    except Exception as e:
        msg_text = f"Oops! Something went wrong: {e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    msg_text = f"{user_mention} was muted by {admin_mention}\n"
    if reason:
        msg_text += f"Reason: `{reason}`\n"
    if time:
        msg_text += f"Duration: `{time}`\n"
    return msg_text, True

async def unmute_user(user_id, first_name, admin_id, admin_name, chat_id):
    """Unmute a user in the chat."""
    msg_text = ""
    try:
        await app.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_polls=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True
            )
        )
        logging.info(f"Unmute: User {user_id} ({first_name}) unmuted by {admin_id} ({admin_name}) in chat {chat_id}.")
    except ChatAdminRequired:
        msg_text = "I need mute rights to perform this action! 😡🥺"
        return msg_text
    except Exception as e:
        msg_text = f"Oops! Something went wrong: {e}"
        return msg_text

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    msg_text = f"{user_mention} was unmuted by {admin_mention}"
    return msg_text

@app.on_message(filters.command(["ban"]))
async def ban_command_handler(client, message):
    """Handle /ban command."""
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name

    has_perm, error_msg = await check_admin_permissions(message, admin_id)
    if not has_perm:
        return await message.reply_text(error_msg)

    user_id, first_name, reason, _ = await extract_user(message)
    if not user_id:
        return await message.reply_text("Please specify a valid user or reply to their message.")

    msg_text, result = await ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
    await message.reply_text(msg_text)

@app.on_message(filters.command(["unban"]))
async def unban_command_handler(client, message):
    """Handle /unban command."""
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name

    has_perm, error_msg = await check_admin_permissions(message, admin_id)
    if not has_perm:
        return await message.reply_text(error_msg)

    user_id, first_name, _, _ = await extract_user(message)
    if not user_id:
        return await message.reply_text("Please specify a valid user or reply to their message.")

    msg_text = await unban_user(user_id, first_name, admin_id, admin_name, chat_id)
    await message.reply_text(msg_text)

@app.on_message(filters.command(["mute"]))
async def mute_command_handler(client, message):
    """Handle /mute command."""
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name

    has_perm, error_msg = await check_admin_permissions(message, admin_id)
    if not has_perm:
        return await message.reply_text(error_msg)

    user_id, first_name, reason, _ = await extract_user(message)
    if not user_id:
        return await message.reply_text("Please specify a valid user or reply to their message.")

    msg_text, result = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
    await message.reply_text(msg_text)

@app.on_message(filters.command(["unmute"]))
async def unmute_command_handler(client, message):
    """Handle /unmute command."""
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name

    has_perm, error_msg = await check_admin_permissions(message, admin_id)
    if not has_perm:
        return await message.reply_text(error_msg)

    user_id, first_name, _, _ = await extract_user(message)
    if not user_id:
        return await message.reply_text("Please specify a valid user or reply to their message.")

    msg_text = await unmute_user(user_id, first_name, admin_id, admin_name, chat_id)
    await message.reply_text(msg_text)

@app.on_message(filters.command(["tmute"]))
async def tmute_command_handler(client, message):
    """Handle /tmute command."""
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name

    has_perm, error_msg = await check_admin_permissions(message, admin_id)
    if not has_perm:
        return await message.reply_text(error_msg)

    user_id, first_name, _, time_str = await extract_user(message)
    if not user_id or not time_str:
        return await message.reply_text("Please specify a valid user and time.\nFormat: /tmute <username> <time> (e.g., 2m, 3h, 1d)")

    mute_duration = parse_duration(time_str)
    if not mute_duration:
        return await message.reply_text("Invalid time format!\nFormat: <number>[m|h|d] (e.g., 2m for 2 minutes)")

    msg_text, result = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason=None, time=mute_duration)
    await message.reply_text(msg_text)
