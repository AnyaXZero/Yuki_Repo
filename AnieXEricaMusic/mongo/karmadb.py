from AnieXEricaMusic import db

karma_collection = db.karma

async def get_karma(chat_id: int, user_id: int) -> int:
    data = await karma_collection.find_one({"chat_id": chat_id, "user_id": user_id})
    return data["karma"] if data else 0

async def update_karma(chat_id: int, user_id: int, change: int):
    await karma_collection.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$inc": {"karma": change}},
        upsert=True
    )
