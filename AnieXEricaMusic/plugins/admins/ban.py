from pyrogram import filters, enums from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions ) from pyrogram.errors.exceptions.bad_request_400 import ( ChatAdminRequired, UserAdminInvalid, BadRequest )

import datetime from AnieXEricaMusic import app

def mention(user, name, mention=True): return f"{name}"

async def get_userid_from_username(username): try: user = await app.get_users(username) except: return None return [user.id, user.first_name]

async def ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason, time=None): try: await app.ban_chat_member(chat_id, user_id) except ChatAdminRequired: return "I need ban rights to do that.", False except UserAdminInvalid: return "I can't ban another admin!", False except Exception as e: if user_id == 6711389550: return "I won't ban myself!", False return f"Error: {e}", False

user_mention = mention(user_id, first_name)
admin_mention = mention(admin_id, admin_name)

msg_text = f"{user_mention} was banned by {admin_mention}\n"
if reason:
    msg_text += f"Reason: `{reason}`\n"
if time:
    msg_text += f"Time: `{time}`\n"
return msg_text, True

async def unban_user(user_id, first_name, admin_id, admin_name, chat_id): try: await app.unban_chat_member(chat_id, user_id) except ChatAdminRequired: return "I need unban rights to do that." except Exception as e: return f"Error: {e}"

return f"{mention(user_id, first_name)} was unbanned by {mention(admin_id, admin_name)}"

async def mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason, time=None): try: until_date = datetime.datetime.now() + time if time else None await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), until_date) except ChatAdminRequired: return "I need mute rights to do that.", False except UserAdminInvalid: return "I can't mute another admin!", False except Exception as e: if user_id == 6664582540: return "I won't mute myself!", False return f"Error: {e}", False

msg_text = f"{mention(user_id, first_name)} was muted by {mention(admin_id, admin_name)}\n"
if reason:
    msg_text += f"Reason: `{reason}`\n"
if time:
    msg_text += f"Time: `{time}`\n"
return msg_text, True

async def unmute_user(user_id, first_name, admin_id, admin_name, chat_id): try: await app.restrict_chat_member( chat_id, user_id, ChatPermissions( can_send_media_messages=True, can_send_messages=True, can_send_other_messages=True, can_send_polls=True, can_add_web_page_previews=True, can_invite_users=True ) ) except ChatAdminRequired: return "I need unmute rights to do that." except Exception as e: return f"Error: {e}"

return f"{mention(user_id, first_name)} was unmuted by {mention(admin_id, admin_name)}"

async def ensure_admin_privileges(message, action): member = await message.chat.get_member(message.from_user.id) if member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]: if member.privileges.can_restrict_members: return True await message.reply_text(f"You don't have permission to {action} someone.") return False

@app.on_message(filters.command(["ban", "unban", "mute", "unmute", "tmute"])) async def moderation_handler(client, message): cmd = message.command[0] action = cmd.lstrip("/") chat_id = message.chat.id admin_id = message.from_user.id admin_name = message.from_user.first_name

if not await ensure_admin_privileges(message, action):
    return

if action in ["ban", "mute"]:
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    elif len(message.command) > 1:
        target = message.command[1]
        try:
            user_id = int(target)
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(target)
            if not user_obj:
                return await message.reply_text("User not found.")
            user_id, first_name = user_obj
        reason = message.text.partition(message.command[1])[2]
    else:
        return await message.reply_text("Specify a user or reply to one.")

    if action == "ban":
        msg, ok = await ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
    else:
        msg, ok = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
    return await message.reply_text(msg)

elif action in ["unban", "unmute"]:
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    elif len(message.command) > 1:
        target = message.command[1]
        try:
            user_id = int(target)
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(target)
            if not user_obj:
                return await message.reply_text("User not found.")
            user_id, first_name = user_obj
    else:
        return await message.reply_text("Specify a user or reply to one.")

    if action == "unban":
        msg = await unban_user(user_id, first_name, admin_id, admin_name, chat_id)
    else:
        msg = await unmute_user(user_id, first_name, admin_id, admin_name, chat_id)
    return await message.reply_text(msg)

elif action == "tmute":
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        time_str = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    elif len(message.command) > 2:
        target, time_str = message.command[1], message.command[2]
        try:
            user_id = int(target)
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(target)
            if not user_obj:
                return await message.reply_text("User not found.")
            user_id, first_name = user_obj
    else:
        return await message.reply_text("Format: /tmute <user> <duration>, e.g. /tmute @user 2m")

    try:
        unit = time_str[-1]
        amount = int(time_str[:-1])
        duration = {"m": datetime.timedelta(minutes=amount), "h": datetime.timedelta(hours=amount), "d": datetime.timedelta(days=amount)}[unit]
    except:
        return await message.reply_text("Invalid format. Use m/h/d, e.g. 5m, 1h, 2d")

    msg, ok = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, None, duration)
    return await message.reply_text(msg)

