from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# 🔗 WebApp linklar
WEBAPP_SOLVE = "https://olimovnarashbot-production.up.railway.app/solve"
WEBAPP_CREATE = "https://olimovnarashbot-production.up.railway.app/create"

# 🔥 ADMIN ID NI QO‘LDA YOZAMIZ (ENV bilan ovora bo‘lmaymiz)
ADMIN_ID = 1981059344


def menu_keyboard(user_id: int):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

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

    # 🔥 ADMIN
    if user_id == ADMIN_ID:
        kb.row(
            KeyboardButton(
                text="✏️ Test yaratish",
                web_app=WebAppInfo(url=WEBAPP_CREATE)
            )
        )

    return kb
