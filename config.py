
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29533034"))
API_HASH = getenv("API_HASH", "e2aa5fe8e0188aee36037d5685e9e8b4")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "8182440075:AAGIFAKZzwGEMEGrhxoVSJXlXYqAnStdpH0")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002392274240))

OWNER_ID = int(getenv("OWNER_ID", 6138142369))

OWNER = int(getenv("OWNER", 6138142369))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Zfini/Adonis",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MidexozBotUpdates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Midexoz")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","BQHCo2oAt6F-mfjiJ6l5HjMyYxANEqSMBAkqcOzqffg_h-cNpOPZUCL6nNVmLuIYSGwZ2IJ0ivhdJsssYwjh1ipMK9JMDjhHs5oyhoDOJhEs3jEdaV7Y6Ignw-uEYebpIUn6PQrEGHgzGEBqPMWJa6fnkX1Ut34ivZu4wuD78cmhpl0Yo1cZcRDgwgRzhxH2AuZwbdHjNT6F926mTtl4ekUHcopnf17AkwQV-vcQwv9gR3OwaG-gIEeapsgDAhLORRakO4NGB9NvDzSqMyNq1iIlZfJelAf1nFRViB3roex_tQ3S2RUNaA8_8iK5pmdNaK6DtH7XUkxWFORQjVHGO08FDo9H4gAAAAHGoxL-AA")
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


START_IMG_URL = getenv("START_IMG_URL", "https://i.ibb.co/CstB6QSJ/photo-2024-03-22-06-52-11-7486776253521854492.jpg")
PING_IMG_URL = "https://files.catbox.moe/h29ssa.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/lad0jq.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://files.catbox.moe/1k8thz.jpg")
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/lk1jy2.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/rp9eg9.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/jmo3i7.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/jmo3i7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"

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
