from AnieXEricaMusic import db

afk = db.afk  # MongoDB collection

async def set_afk(user_id: int, reason: str):
    await afk.update_one({"_id": user_id}, {"$set": {"reason": reason}}, upsert=True)

async def get_afk(user_id: int):
    return await afk.find_one({"_id": user_id})

async def remove_afk(user_id: int):
    await afk.delete_one({"_id": user_id})
