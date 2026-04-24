from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from bot.config import ADMIN_ID

# 🔗 WebApp linklar
WEBAPP_SOLVE = "https://olimovnarashbot-production.up.railway.app/solve"
WEBAPP_CREATE = "https://olimovnarashbot-production.up.railway.app/create"


def menu_keyboard(user_id=None):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    # 📤 Javob yuborish → WebApp
    kb.row(
        KeyboardButton(
            text="📤 Javob yuborish",
            web_app=WebAppInfo(url=WEBAPP_SOLVE)
        ),
        KeyboardButton("📊 Mening natijalarim")
    )

    # 👤 Profil / ℹ️ haqida
    kb.row(
        KeyboardButton("👤 Profil"),
        KeyboardButton("ℹ️ Bot haqida")
    )

    # 🔥 ADMIN TEKSHIRUV (100% ishlaydi)
    if str(user_id) == str(ADMIN_ID):
        kb.row(
            KeyboardButton(
                text="✏️ Test yaratish",
                web_app=WebAppInfo(url=WEBAPP_CREATE)
            )
        )

    return kb
