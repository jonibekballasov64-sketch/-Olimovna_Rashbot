from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row(
        KeyboardButton("📤 Javob yuborish"),
        KeyboardButton("📊 Mening natijalarim")
    )
    kb.row(
        KeyboardButton("👤 Profil"),
        KeyboardButton("ℹ️ Bot haqida")
    )

    return kb
