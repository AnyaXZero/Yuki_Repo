from pyrogram import filters, enums 
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions ) 
from pyrogram.errors.exceptions.bad_request_400 import ( ChatAdminRequired, UserAdminInvalid, BadRequest )

import datetime from AnieXEricaMusic import app

def mention(user, name, mention=True): return f"{name}"

async def get_userid_from_username(username): try: user = await app.get_users(username) except: return None return [user.id, user.first_name]

async def ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason, time=None): try: await app.ban_chat_member(chat_id, user_id) except ChatAdminRequired: return "I need ban rights to do that!", False except UserAdminInvalid: return "I won't ban an admin!", False except Exception as e: if user_id == 6711389550: return "Why should I ban myself?", False return f"Oops!!\n{e}", False

user_mention = mention(user_id, first_name)
admin_mention = mention(admin_id, admin_name)
msg_text = f"{user_mention} was banned by {admin_mention}\n"
if reason:
    msg_text += f"Reason: `{reason}`\n"
if time:
    msg_text += f"Time: `{time}`\n"
return msg_text, True

async def unban_user(user_id, first_name, admin_id, admin_name, chat_id): try: await app.unban_chat_member(chat_id, user_id) except ChatAdminRequired: return "I need unban rights to do that!" except Exception as e: return f"Oops!!\n{e}"

user_mention = mention(user_id, first_name)
admin_mention = mention(admin_id, admin_name)
return f"{user_mention} was unbanned by {admin_mention}"

async def mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason, time=None): try: if time: mute_end_time = datetime.datetime.now() + time await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), mute_end_time) else: await app.restrict_chat_member(chat_id, user_id, ChatPermissions()) except ChatAdminRequired: return "I need mute rights to do that!", False except UserAdminInvalid: return "I won't mute an admin!", False except Exception as e: if user_id == 6664582540: return "Why should I mute myself?", False return f"Oops!!\n{e}", False

user_mention = mention(user_id, first_name)
admin_mention = mention(admin_id, admin_name)
msg_text = f"{user_mention} was muted by {admin_mention}\n"
if reason:
    msg_text += f"Reason: `{reason}`\n"
if time:
    msg_text += f"Time: `{time}`\n"
return msg_text, True

async def unmute_user(user_id, first_name, admin_id, admin_name, chat_id): try: await app.restrict_chat_member( chat_id, user_id, ChatPermissions( can_send_media_messages=True, can_send_messages=True, can_send_other_messages=True, can_send_polls=True, can_add_web_page_previews=True, can_invite_users=True ) ) except ChatAdminRequired: return "I need unmute rights to do that!" except Exception as e: return f"Oops!!\n{e}"

user_mention = mention(user_id, first_name)
admin_mention = mention(admin_id, admin_name)
return f"{user_mention} was unmuted by {admin_mention}"

async def kick_user(user_id, first_name, admin_id, admin_name, chat_id, reason=None): try: await app.ban_chat_member(chat_id, user_id) await app.unban_chat_member(chat_id, user_id) except ChatAdminRequired: return "I need kick rights to do that!", False except UserAdminInvalid: return "I won't kick an admin!", False except Exception as e: return f"Oops!!\n{e}", False

user_mention = mention(user_id, first_name)
admin_mention = mention(admin_id, admin_name)
msg_text = f"{user_mention} was kicked by {admin_mention}\n"
if reason:
    msg_text += f"Reason: `{reason}`\n"
return msg_text, True

@app.on_message(filters.command("kick")) async def kick_command_handler(client, message): chat_id = message.chat.id admin_id = message.from_user.id admin_name = message.from_user.first_name member = await message.chat.get_member(admin_id) if member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER] or not member.privileges.can_restrict_members: return await message.reply_text("You don't have permission to kick someone")

if message.reply_to_message:
    user_id = message.reply_to_message.from_user.id
    first_name = message.reply_to_message.from_user.first_name
    reason = message.text.split(None, 1)[1] if len(message.command) > 1 else None
elif len(message.command) > 1:
    try:
        user_id = int(message.command[1])
        first_name = "User"
    except:
        user_obj = await get_userid_from_username(message.command[1])
        if user_obj is None:
            return await message.reply_text("I can't find that user")
        user_id, first_name = user_obj
    reason = message.text.partition(message.command[1])[2].strip()
else:
    return await message.reply_text("Please reply to a user or provide a username/user ID")

msg_text, result = await kick_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
await message.reply_text(msg_text)

# existing ban, unban, mute, unmute, tmute command handlers remain unchanged...
