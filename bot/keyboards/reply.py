from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

WEBAPP_SOLVE = "https://olimovnarashbot-production.up.railway.app/solve"
WEBAPP_CREATE = "https://olimovnarashbot-production.up.railway.app/create"

ADMIN_ID = 1981059344


def menu_keyboard(user_id: int):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    # 🔥 TO‘G‘RIDAN-TO‘G‘RI WEB APP
    kb.row(
        KeyboardButton(
            text="✅ Javob yuborish",
            web_app=WebAppInfo(url=WEBAPP_SOLVE)
        ),
        KeyboardButton("📊 Mening natijalarim")
    )

    kb.row(
        KeyboardButton("👤 Profil"),
        KeyboardButton("ℹ️ Bot haqida")
    )

    # 🔥 ADMIN
    if int(user_id) == int(ADMIN_ID):
        kb.row(
            KeyboardButton(
                text="➕ Test yaratish",
                web_app=WebAppInfo(url=WEBAPP_CREATE)
            )
        )

    return kb
