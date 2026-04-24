from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# 🔗 WebApp linklar
WEBAPP_SOLVE = "https://olimovnarashbot-production.up.railway.app/solve"
WEBAPP_CREATE = "https://olimovnarashbot-production.up.railway.app/create"


def menu_keyboard(user_id: int):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    # 📤 JAVOB YUBORISH
    kb.row(
        KeyboardButton(
            text="📤 Javob yuborish",
            web_app=WebAppInfo(url=WEBAPP_SOLVE)
        ),
        KeyboardButton("📊 Mening natijalarim")
    )

    # 👤 / ℹ️
    kb.row(
        KeyboardButton("👤 Profil"),
        KeyboardButton("ℹ️ Bot haqida")
    )

    # 🔥 ADMIN (TO‘G‘RILANDI)
    if str(user_id) == "1981059344":
        kb.row(
            KeyboardButton(
                text="✏️ Test yaratish",
                web_app=WebAppInfo(url=WEBAPP_CREATE)
            )
        )

    return kb
