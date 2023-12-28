import re, logging
from os import environ
from Script import script
from dotenv import load_dotenv
load_dotenv()


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '1234'))
API_HASH = environ.get('API_HASH', '1234567')
BOT_TOKEN = environ.get('BOT_TOKEN', '1234:abcd')

#FOR 2ND BOT ENV👇👇
ANUSHKA_BOT_TOKEN = environ.get('ANUSHKA_BOT_TOKEN', '1234:abcd') # for your 2nd bot

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/0d6ebe52d573e683ad3cd.jpg https://graph.org/file/d7f16e8380808e76e6572.jpg https://graph.org/file/4f1718c6836798e340e06.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/d7f16e8380808e76e6572.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/ae0330a1236c2143e8074.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/d7f16e8380808e76e6572.jpg")

#2nd BOT SETTINGS 👇👇
ANUSHKA_CACHE_TIME = int(environ.get('ANUSHKA_CACHE_TIME', 300))
ANUSHKA_USE_CAPTION_FILTER = bool(environ.get('ANUSHKA_USE_CAPTION_FILTER', True))

ANUSHKA_PICS = (environ.get('ANUSHKA_PICS', 'https://graph.org/file/1aabc32de4442dbc5a2a0.jpg https://graph.org/file/9458bd38633097021468e.jpg https://graph.org/file/b352b109ff6ab64a0dec5.jpg https://graph.org/file/1e58ec7e88373d43fe698.jpg https://graph.org/file/e29fe074270cda1833462.jpg https://graph.org/file/ce952c92d4c42fd588213.jpg https://graph.org/file/5ee19f028c4585af12b6c.jpg https://graph.org/file/41dfb4d472208520d0314.jpg https://graph.org/file/ca6de43379db0999546ad.jpg https://graph.org/file/2212ca8121a17edb5a2e7.jpg')).split()
ANUSHKA_NOR_IMG = environ.get("ANUSHKA_NOR_IMG", "https://graph.org/file/073f11f799747248a2d9c.jpg")
ANUSHKA_MELCOW_VID = environ.get("ANUSHKA_MELCOW_VID", "https://graph.org/file/9712f22f0fb0edc2e2438.mp4")
ANUSHKA_SPELL_IMG = environ.get("ANUSHKA_SPELL_IMG", "https://graph.org/file/073f11f799747248a2d9c.jpg")


# Admins, Channels & User
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1927155351').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002029599178')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

#FOR 2ND BOT ADMIN & ALL 👇👇
ANUSHKA_ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ANUSHKA_ADMINS', '1927155351').split()]
ANUSHKA_CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('ANUSHKA_CHANNELS', '').split()]
anushka_auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('ANUSHKA_AUTH_USERS', '').split()]
ANUSHKA_AUTH_USERS = (anushka_auth_users + ADMINS) if auth_users else []
anushka_auth_grp = environ.get('ANUSHKA_AUTH_GROUP')
ANUSHKA_AUTH_GROUPS = [int(ch) for ch in anushka_auth_grp.split()] if anushka_auth_grp else None
anushka_support_chat_id = environ.get('ANUSHKA_SUPPORT_CHAT_ID')
anushka_reqst_channel = environ.get('ANUSHKA_REQST_CHANNEL_ID')
ANUSHKA_REQST_CHANNEL = int(anushka_reqst_channel) if anushka_reqst_channel and id_pattern.search(anushka_reqst_channel) else None
ANUSHKA_SUPPORT_CHAT_ID = int(anushka_support_chat_id) if anushka_support_chat_id and id_pattern.search(anushka_support_chat_id) else None

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")
ANUSHKA_DOWNLOAD_LOCATION = environ.get("ANUSHKA_DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
ANUSHKA_TMP_DOWNLOAD_DIRECTORY = environ.get("ANUSHKA_TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
# Open AI
OPENAI_API = environ.get('OPENAI_API', '0')
ANUSHKA_OPENAI_API = environ.get('ANUSHKA_OPENAI_API', '0')

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
ANUSHKA_COMMAND_HAND_LER = environ.get("ANUSHKA_COMMAND_HAND_LER", "/")
# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "FreyaAllan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# 2nd Bot DB
ANUSHKA_DATABASE_URI = environ.get('ANUSHKA_DATABASE_URI', DATABASE_URI)
ANUSHKA_DATABASE_NAME = environ.get('ANUSHKA_DATABASE_NAME', "ANUSHKA")
ANUSHKA_COLLECTION_NAME = environ.get('ANUSHKA_COLLECTION_NAME', 'Telegram_files')

# stickers
STICKERS = (environ.get('STICKERS', 'CAACAgQAAxkBAAECj2llfiIoK0pPHx7cqiyukXHMt5v1-AACoBIAAqbJ8VN_VFM-pJqvRB4E CAACAgQAAxkBAAECj2xlfiJX6TDOR1DSBpBvsHydXPSj4gACixEAAgdC8VOWMsK5U3LDah4E CAACAgQAAxkBAAECj29lfiJzIEt9B8wla9p7n2HH9nMGsQACxBAAAmrg8VP8x6W5qltX8h4E')).split()

#2nd Sticker
ANUSHKA_STICKERS = (environ.get('STICKERS', 'CAACAgQAAxkBAAECj2BlfiBOeO3D8RCEUwayhRTicL-CagACchQAAh7r8VNOUQkfOMsYdh4E CAACAgQAAxkBAAECj2NlfiEdPQMYtQdWBxjciJrYbWayhwAC3w4AAmT98FPFzDUju0qquh4E CAACAgQAAxkBAAECj2ZlfiEspMWN06hnP_JWCxJH3WN0-gACvREAAiEX8FOiQhsHb2aFex4E')).split()

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", "")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

anushka_auth_channel = environ.get('ANUSHKA_AUTH_CHANNEL')
ANUSHKA_AUTH_CHANNEL = int(anushka_auth_channel) if anushka_auth_channel and id_pattern.search(anushka_auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
ANUSHKA_REQ_CHANNEL = environ.get("ANUSHKA_REQ_CHANNEL", "")
ANUSHKA_REQ_CHANNEL = int(ANUSHKA_REQ_CHANNEL) if ANUSHKA_REQ_CHANNEL and id_pattern.search(ANUSHKA_REQ_CHANNEL) else False
ANUSHKA_JOIN_REQS_DB = environ.get("ANUSHKA_JOIN_REQS_DB", DATABASE_URI)

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

ANUSHKA_CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
ANUSHKA_TEXT = environ.get("ANUSHKA_APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.</b>")
ANUSHKA_APPROVED = environ.get("ANUSHKA_APPROVED_WELCOME", "on").lower()

# Others
IS_VERIFY = bool(environ.get('IS_VERIFY', False))
VERIFY2_URL = environ.get('VERIFY2_URL', "tnshort.net")
VERIFY2_API = environ.get('VERIFY2_API', "0c8ebd63bfe9f67f9970b8767498ff60316b9b03")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'Onepagelink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '8c09653e5c38f84d1b76ad3197c5a023e53b494d')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
S_GROUP = environ.get('S_GROUP',"https://telegram.me/BotszSupport")
RUL_LNK = environ.get('RUL_LNK',"https://graph.org/%F0%9D%97%A0%F0%9D%9E%93%F0%9D%97%A6%F0%9D%97%A7%F0%9D%9E%9D%F0%9D%97%A5-02-15")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://telegram.me/NobiDeveloper")
GRP_LNK = environ.get('GRP_LNK', 'https://telegram.me/BotszSupport')
CHNL_LNK = environ.get('CHNL_LNK', 'https://telegram.me/BotszList')
OWN_LNK = environ.get('S_GROUP',"https://telegram.me/NobiDeveloperr")
MVG_LNK = environ.get('S_GROUP',"https://telegram.me/AllRequestGroups")
MSG_ALRT = environ.get('MSG_ALRT', 'ꜱʜᴀʀᴇ  ᴀɴᴅ  ꜱᴜᴘᴘᴏʀᴛ  ᴜꜱ')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'BotszSupport')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["hindi", "hin", "tamil", "tam", "telugu", "tel", "english", "eng", "kannada", "kan", "malayalam", "mal"]
TUTORIAL = environ.get('TUTORIAL', 'https://youtu.be/rddlpYLm0G0')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))

ANUSHKA_IS_VERIFY = bool(environ.get('ANUSHKA_IS_VERIFY', False))
ANUSHKA_VERIFY2_URL = environ.get('ANUSHKA_VERIFY2_URL', "tnshort.net")
ANUSHKA_VERIFY2_API = environ.get('ANUSHKA_VERIFY2_API', "0c8ebd63bfe9f67f9970b8767498ff60316b9b03")
ANUSHKA_SHORTLINK_URL = environ.get('ANUSHKA_SHORTLINK_URL', 'Onepagelink.in')
ANUSHKA_SHORTLINK_API = environ.get('ANUSHKA_SHORTLINK_API', '8c09653e5c38f84d1b76ad3197c5a023e53b494d')
ANUSHKA_IS_SHORTLINK = bool(environ.get('ANUSHKA_IS_SHORTLINK', True))
ANUSHKA_NO_RESULTS_MSG = bool(environ.get('ANUSHKA_NO_RESULTS_MSG', True))
ANUSHKA_DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('ANUSHKA_DELETE_CHANNELS', '0').split()]
ANUSHKA_MAX_B_TN = environ.get("ANUSHKA_MAX_B_TN", "8")
ANUSHKA_MAX_BTN = is_enabled((environ.get('ANUSHKA_MAX_BTN', "True")), True)
ANUSHKA_PORT = environ.get("ANUSHKA_PORT", "8080")
ANUSHKA_S_GROUP = environ.get('ANUSHKA_S_GROUP',"https://telegram.me/BotszSupport")
ANUSHKA_RUL_LNK = environ.get('ANUSHKA_RUL_LNK',"https://graph.org/%F0%9D%97%A0%F0%9D%9E%93%F0%9D%97%A6%F0%9D%97%A7%F0%9D%9E%9D%F0%9D%97%A5-02-15")
ANUSHKA_MAIN_CHANNEL = environ.get('ANUSHKA_MAIN_CHANNEL',"https://telegram.me/NobiDeveloper")
ANUSHKA_GRP_LNK = environ.get('ANUSHKA_GRP_LNK', 'https://telegram.me/BotszSupport')
ANUSHKA_CHNL_LNK = environ.get('ANUSHKA_CHNL_LNK', 'https://telegram.me/BotszList')
ANUSHKA_OWN_LNK = environ.get('ANUSHKA_S_GROUP',"https://telegram.me/NobiDeveloperr")
ANUSHKA_MVG_LNK = environ.get('ANUSHKA_S_GROUP',"https://telegram.me/AllRequestGroups")
ANUSHKA_MSG_ALRT = environ.get('ANUSHKA_MSG_ALRT', 'ꜱʜᴀʀᴇ  ᴀɴᴅ  ꜱᴜᴘᴘᴏʀᴛ  ᴜꜱ')
ANUSHKA_LOG_CHANNEL = int(environ.get('ANUSHKA_LOG_CHANNEL', LOG_CHANNEL))
ANUSHKA_SUPPORT_CHAT = environ.get('ANUSHKA_SUPPORT_CHAT', 'BotszSupport')
ANUSHKA_P_TTI_SHOW_OFF = is_enabled((environ.get('ANUSHKA_P_TTI_SHOW_OFF', "True")), True)
ANUSHKA_IMDB = is_enabled((environ.get('ANUSHKA_IMDB', "False")), False)
ANUSHKA_AUTO_FFILTER = is_enabled((environ.get('ANUSHKA_AUTO_FFILTER', "True")), True)
ANUSHKA_AUTO_DELETE = is_enabled((environ.get('ANUSHKA_AUTO_DELETE', "True")), True)
ANUSHKA_SINGLE_BUTTON = is_enabled((environ.get('ANUSHKA_SINGLE_BUTTON', "True")), True)
ANUSHKA_CUSTOM_FILE_CAPTION = environ.get("ANUSHKA_CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
ANUSHKA_BATCH_FILE_CAPTION = environ.get("ANUSHKA_BATCH_FILE_CAPTION", None)
ANUSHKA_IMDB_TEMPLATE = environ.get("ANUSHKA_IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
ANUSHKA_LONG_IMDB_DESCRIPTION = is_enabled(environ.get("ANUSHKA_LONG_IMDB_DESCRIPTION", "False"), False)
ANUSHKA_SPELL_CHECK_REPLY = is_enabled(environ.get("ANUSHKA_SPELL_CHECK_REPLY", "True"), True)
ANUSHKA_MAX_LIST_ELM = environ.get("ANUSHKA_MAX_LIST_ELM", None)
ANUSHKA_INDEX_REQ_CHANNEL = int(environ.get('ANUSHKA_INDEX_REQ_CHANNEL', LOG_CHANNEL))
ANUSHKA_FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('ANUSHKA_FILE_STORE_CHANNEL', '')).split()]
ANUSHKA_MELCOW_NEW_USERS = is_enabled((environ.get('ANUSHKA_MELCOW_NEW_USERS', "True")), True)
ANUSHKA_PROTECT_CONTENT = is_enabled((environ.get('ANUSHKA_PROTECT_CONTENT', "False")), False)
ANUSHKA_PUBLIC_FILE_STORE = is_enabled((environ.get('ANUSHKA_PUBLIC_FILE_STORE', "True")), True)

ANUSHKA_LANGUAGES = ["hindi", "hin", "tamil", "tam", "telugu", "tel", "english", "eng", "kannada", "kan", "malayalam", "mal"]
ANUSHKA_TUTORIAL = environ.get('ANUSHKA_TUTORIAL', 'https://youtu.be/rddlpYLm0G0')
ANUSHKA_IS_TUTORIAL = bool(environ.get('ANUSHKA_IS_TUTORIAL', True))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
