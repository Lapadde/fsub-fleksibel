from fsub import Bot

from hydrogram import filters
from hydrogram.types import CallbackQuery, InlineKeyboardMarkup, Message
from hydrogram.types import InlineKeyboardButton


class Data:
    HELP = """
/start: Mulai bot
/help: Bantuan dan tentang bot
/ping: Cek latensi bot
/uptime: Cek waktu aktif bot
/users: Statistik pengguna bot (Admin)
/batch: Multi post dalam satu link (Admin)
/broadcast: Pesan siaran ke pengguna bot (Admin)
"""

    close = [
        [InlineKeyboardButton("〤 ᴛᴜᴛᴜᴘ 〤", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʙᴀɴᴛᴜᴀɴ", callback_data="help"),
            InlineKeyboardButton("〤 ᴛᴜᴛᴜᴘ 〤", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴊᴀsᴀ ᴘᴇᴍʙᴜᴀᴛᴀɴ ʙᴏᴛ ✓", url=f"https://t.me/baksdudee"),
            InlineKeyboardButton("Tutup", callback_data="close")
        ],
    ]

    ABOUT = """
@{} adalah Bot untuk menyimpan postingan atau file yang dapat diakses melalui link khusus.

  Framework: <a href='https://docs.hydrogram.org'>hydrogram</a>
  Jasa Deploy BOT: <a href='https://t.me/baksdudee'>Klik Disini</a>
"""


@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def help(client: Bot, message: Message):
    await client.send_message(
        message.chat.id, 
        Data.HELP,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )


@Bot.on_callback_query()
async def handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        try:
            await query.message.edit_text(
                text=Data.ABOUT.format(client.username),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.mbuttons),
            )
        except Exception:
            pass
    elif data == "help":
        try:
            await query.message.edit_text(
                text=Data.HELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
        except Exception:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass