
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "25955854"))
API_HASH = getenv("API_HASH", "2ede59823a90cb31442a74f5ae01f675")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7979900579:AAFqBNSz_nOxXtyDcObsI8kUS56jMSdxrio")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://shigarakisan:demnkin@cluster0.cxt4iov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002392274240))

OWNER_ID = int(getenv("OWNER_ID", 6018803920))

OWNER = int(getenv("OWNER", 6018803920))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Zfini/Adonis",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MBT_UPDATES")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+ytk9hkZfGjY3MDRl")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","BQFTgqgABbPDrCGjUZHIsuiw1XNSNW2VAj8xwZRnaobyMkStn_S1rQagcvCEo88IhMUCucAEgH10yPzGwR2Rziq_NLkaKrsBAI6fcgWT9cKEdZfRK31mP3SkL5lMKEeO4ghX_5wvKkFdB7R9fsB_Vc3QhcybIfdIxe7bgvFYuvXQPLSucve-ZW-TA1-3Z9zhgZdxR04vXZwBGF4KhaX47ia_2_8p6uzFeqLHjptaYv7aSrT1zxrxG5K6YzNK0R3uof8R_gzV18B2B2GKzYa6hFFG5SWpFI789HWmxNt3Jgva2QTi7UMahIqQ9Oj1s6suER9JytTR5pXQjma9II7jwJuU21hglgAAAAHUsVFIAA")
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


START_IMG_URL =  "https://files.catbox.moe/iffmnv.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
STATS_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/f3yuiy.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/urv7wi.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/2tcim5.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/jkqyg2.jpg"

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
