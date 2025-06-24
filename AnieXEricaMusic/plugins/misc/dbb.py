from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://YukiMusic:Yukimusicbot@cluster0.mvqpp8v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_URI)
db = client["YukiMusic"]  # your database name
