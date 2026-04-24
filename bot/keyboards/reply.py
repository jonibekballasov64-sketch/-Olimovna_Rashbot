from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from bot.config import ADMIN_ID

WEBAPP_SOLVE = "https://olimovnarashbot-production.up.railway.app/solve"
WEBAPP_CREATE = "https://olimovnarashbot-production.up.railway.app/create"


def menu_keyboard(user_id=None):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    # 🔥 JAVOB YUBORISH → WEBAPP
    kb.row(
        KeyboardButton(
            text="📤 Javob yuborish",
            web_app=WebAppInfo(url=WEBAPP_SOLVE)
        ),
        KeyboardButton("📊 Mening natijalarim")
    )

    kb.row(
        KeyboardButton("👤 Profil"),
        KeyboardButton("ℹ️ Bot haqida")
    )

    # 🔥 ADMIN BO‘LSA
    if user_id == ADMIN_ID:
        kb.row(
            KeyboardButton(
                text="✏️ Test yaratish",
                web_app=WebAppInfo(url=WEBAPP_CREATE)
            )
        )

    return kb
