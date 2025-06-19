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

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002567836754))

OWNER_ID = int(getenv("OWNER_ID", 7595051499))

OWNER = int(getenv("OWNER", 7595051499))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","yuki")

HEROKU_API_KEY = getenv("HRKU-AA5DN1qAs5A9A42MDd_gRIvcP5e15YTpWZ8nXVvDsdNw_____wPkb01lB0Gk")

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

STRING1 = getenv("STRING_SESSION","AQG166IAQhs2knmC7b0pAM7Z0mY8pyVnfWJtKo4shFAORQ5BS3g7vI0oafkQ5AdJcIERzRpz2JuwUWDKW77rshkVZ2LGB_9HUL3s04mhHT7kbOC8mQQQ_4-KBDHHD8YcPUE4tdfBXks7KR1flyI-OqGji_jrEstfFMsqm-ebqgV1yHvvk5PvwBgxt6UhG6b1Fum1qYLnnprRFq3vnmV4ccFKlb2Y66ffJi9u3lc874rS3U0jfXoiv0XkML2rSP_F-pggv8jMOqQWbJIECaxqyIKPghWVDCJDnMb7T071Ortga1e4XsL81LI5vDV0DzIFyj7yRY5Pys5pVOvH1A_FIIys5LrYNgAAAAHNtx3RAA")
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


START_IMG_URL =  "https://files.catbox.moe/bhy0ks.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/vyxlxz.jpg"
STATS_IMG_URL = "https://files.catbox.moe/n1ltse.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ra02su.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/fxt5ej.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/22ornp.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/90o1js.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/g20jh4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2f7qbx.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/y5hhpd.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ac40y5.jpg"

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

