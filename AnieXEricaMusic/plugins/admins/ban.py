from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)

import datetime
from AnieXEricaMusic.core.call import app




def mention(user, name, mention=True):
    if mention:
        return f"[{name}](tg://openmessage?user_id={user})"
    else:
        return f"[{name}](https://t.me/{user})"

async def get_userid_from_username(username):
    try:
        user = await app.get_users(username)
    except:
        return None
    return [user.id, user.first_name]

async def bans_user(user_id, first_name, admin_id, admin_name, chat_id, message):
    try:
        await app.ban_chat_member(chat_id, user_id)
        await app.unban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        return "I need ban rights to perform this action.", False
    except UserAdminInvalid:
        return "I can't ban another admin!", False
    except Exception as e:
        if user_id == OWNER_ID:
            return "Why should I ban myself? I'm not that silly!", False
        return f"An error occurred: {e}", False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    await app.send_message(LOG_GROUP_ID, f"{user_mention} was banned by {admin_mention} in {message.chat.title}")
        return ban_message, True

@app.on_message(filters.command("ban") & admin_filter)
async def ban_user_with_unban_button(client, message):
    chat = message.chat
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    
    if member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        if not member.privileges.can_restrict_members:
            return await message.reply_text("You don't have permission to ban someone.")
    else:
        return await message.reply_text("You don't have permission to ban someone.")
        
    if len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except ValueError:
            user_obj = await get_userid_from_username(message.command[1])
            if user_obj is None:
                return await message.reply_text("User not found.")
            user_id = user_obj[0]
            first_name = user_obj[1]
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    else:
        return await message.reply_text("Please specify a valid user or reply to their message.")
        
    msg_text, result = await bans_user(user_id, first_name, admin_id, admin_name, chat_id, message)
    if not result:
        return await message.reply_text(msg_text)

    unban_button = [
        [InlineKeyboardButton("ƲɴʙᴀƝ ƲsᴇƦ", callback_data=f"unban_{user_id}")]
    ]
    await message.reply_text(
        f"Click below to unban {first_name}.",
        reply_markup=InlineKeyboardMarkup(unban_button),
    )

@app.on_message(filters.command("unban") & admin_filter)
async def unban_user(client, message):
    chat = message.chat
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    
    if member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        if not member.privileges.can_restrict_members:
            return await message.reply_text("You don't have permission to unban someone.")
    else:
        return await message.reply_text("You don't have permission to unban someone.")
        
    if len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except ValueError:
            user_obj = await get_userid_from_username(message.command[1])
            if user_obj is None:
                return await message.reply_text("User not found.")
            user_id = user_obj[0]
            first_name = user_obj[1]
    else:
        return await message.reply_text("Please specify a valid user to unban.")
    
    try:
        await app.unban_chat_member(chat_id, user_id)
        user_mention = mention(user_id, first_name)
        admin_mention = mention(admin_id, admin_name)
        await message.reply_photo(
            photo=random.choice(kickpic),
            caption=f"{user_mention} was unbanned by {admin_mention}.",
            reply_markup=InlineKeyboardMarkup(button),
        )
        await app.send_message(LOG_GROUP_ID, f"{user_mention} was unbanned by {admin_mention} in {message.chat.title}")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

@app.on_callback_query(filters.regex(r"unban_(\d+)"))
async def unban_button_callback(client, callback_query):
    user_id = int(callback_query.matches[0].group(1))
    chat_id = callback_query.message.chat.id
    try:
        await app.unban_chat_member(chat_id, user_id)
        await callback_query.answer("User has been unbanned!")
        await callback_query.message.edit_text("The user has been successfully unbanned.")
    except Exception as e:
        await callback_query.answer(f"An error occurred: {e}")

@app.on_message(filters.command("kickme") & filters.group)
async def kickme_command(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chat_id = message.chat.id

    try:
        await app.ban_chat_member(chat_id, user_id)
        await message.reply_photo(
            photo=random.choice(kickpic),
            caption=f"{user_name} has kicked themselves out of the group!",
            reply_markup=InlineKeyboardMarkup(button),
        )
        await app.send_message(LOG_GROUP_ID, f"{user_name} used the kickme command in {message.chat.title}")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

@app.on_message(filters.command("mute"))
@admin_required("can_restrict_members")
async def mute_cmd(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_usage("mute"))

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return
    mem = await _get_member_safe(client, message.chat.id, uid)
    if mem and mem.status == enums.ChatMemberStatus.RESTRICTED and mem.permissions == _DEF_MUTE_PERMS:
        return await message.reply_text("User is already muted.")

    try:
        await client.restrict_chat_member(message.chat.id, uid, _DEF_MUTE_PERMS)
        await message.reply_text(_format_success("Mute", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("I need mute permissions.")
    except UserAdminInvalid:
        await message.reply_text("I cannot mute an admin.")

@app.on_message(filters.command("unmute"))
@admin_required("can_restrict_members")
async def unmute_cmd(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_usage("unmute"))

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return
    mem = await _get_member_safe(client, message.chat.id, uid)
    if not mem or mem.status != enums.ChatMemberStatus.RESTRICTED:
        return await message.reply_text("User is not muted.")

    perms = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
    )
    try:
        await client.restrict_chat_member(message.chat.id, uid, perms)
        await message.reply_text(_format_success("Unmute", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("I need unmute permissions.")

@app.on_message(filters.command("kickme"))
async def kickme_cmd(client, message: Message):
    if message.chat.type == enums.ChatType.PRIVATE:
        return
    try:
        await client.ban_chat_member(message.chat.id, message.from_user.id)
        await asyncio.sleep(3)
        await client.unban_chat_member(message.chat.id, message.from_user.id)
        await message.reply_text("Kicked so hard, your ancestors felt it. 👟💥")
    except ChatAdminRequired:
        await message.reply_text("I need ban permissions.")

@app.on_message(filters.command("kick"))
@admin_required("can_restrict_members")
async def kick_cmd(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_usage("kick"))

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return
    try:
        await client.ban_chat_member(message.chat.id, uid)
        await asyncio.sleep(2)
        await client.unban_chat_member(message.chat.id, uid)
        await message.reply_text(_format_success("Kick", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("I need ban permissions.")
    except UserAdminInvalid:
        await message.reply_text("I cannot kick an admin.")

@app.on_message(filters.command("sban"))
@admin_required("can_restrict_members")
async def sban_cmd(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_usage("sban"))

    uid, _, _ = await extract_user_and_reason(message, client)
    if not uid:
        return
    try:
        await client.ban_chat_member(message.chat.id, uid)
        await message.delete()  # silent
    except ChatAdminRequired:
        await message.reply_text("I need ban permissions.")
    except UserAdminInvalid:
        await message.reply_text("I cannot ban an admin.")
