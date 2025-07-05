import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28699554"))
API_HASH = getenv("API_HASH", "fe1aebd2126aa99df66396123eba8495")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7711734310:AAGZgPru-6Trx1tbeBfWmBjKUwp9qk020fs")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://YukiMusic:Yukimusicbot@cluster0.mvqpp8v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))
BOT_USERNAME = getenv("BOT_USERNAME", "shivang_mishra_op")
BOT_NAME = getenv("BOT_NAME", " 𝙼ᴜsɪᴄ˼ ♪")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002567836754))

OWNER_ID = int(getenv("OWNER_ID", 7595051499))

OWNER = int(getenv("OWNER", 7595051499))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","yuki")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-AA5DN1qAs5A9A42MDd_gRIvcP5e15YTpWZ8nXVvDsdNw_wPkb01lB0Gk")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnyaXZero/Yuki_Repo",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HutaoUpdates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+C0s3qb7sRZA0ZjRk")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","AQG166IAuOvP5ZOn84zcz1vgC5Qt8jwEH3FiVtUdRAh8LUaS26NJ6pcP1H0lVES1HfBr43uuIgTAH_-cdFQ8iBPGi9RMEVHn4cuACXUCSmsIYDwud7mHzRsB9wKPBEcNLrr9bq6hyCIjCd3aGviJwQbrNVDJCWt8prXC6vNTUj07F54kP7d5jnXZ8o5suK22Y2vKJXTYupV9bl8fHpkTmeBo2_f4yDsBnaXbbUdhJfJ2erZhHyay5fKuNsU89rg_fIB_viGaR5kM6KI_Y5N76oZp76tAWip9k4rZfo3I-2Z7AkmYSnVoVGFnmVl2hRg1UlPc22Y1un9CK9Pp9eO5-KYXa9GVWwAAAAHNtx3RAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL =  "https://i.ibb.co/Qvr6qcDr/photo-2025-07-04-14-18-13-7523230930907955204.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/h1CjcZLN/photo-2025-07-04-14-20-06-7523231411944292356.jpg"
STATS_IMG_URL = "https://i.ibb.co/svkYB8wq/photo-2025-07-04-12-56-14-7523209795373891604.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/3mm0819P/photo-2025-07-04-14-03-09-7523227035372617768.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/HpYVtqph/photo-2025-07-04-13-11-14-7523213673729359928.jpg"
STREAM_IMG_URL = "https://i.ibb.co/0ySKjJzZ/photo-2025-07-04-12-55-45-7523209662229905432.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/6dcpT9j/photo-2025-07-04-12-53-06-7523208996509974548.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/qM21YB4H/photo-2025-07-04-13-35-21-7523219871367168032.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/Z1604yPw/photo-2025-07-04-13-34-57-7523219768287952936.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/35ZzPV54/photo-2025-07-04-13-34-24-7523219635143966724.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/8LdFNVJZ/photo-2025-07-04-12-55-08-7523209511906050056.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
COMMAND_PREFIXES = ["/", "!", "."]

