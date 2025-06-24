def mention(user_id: int, name: str) -> str:
    return f"[{name}](tg://openmessage?user_id={user_id})"
