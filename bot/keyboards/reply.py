from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.config import ADMIN_ID


def menu_keyboard(user_id=None):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row(
        KeyboardButton("📤 Javob yuborish"),
        KeyboardButton("📊 Mening natijalarim")
    )
    kb.row(
        KeyboardButton("👤 Profil"),
        KeyboardButton("ℹ️ Bot haqida")
    )

    # 🔥 ADMIN BO‘LSA QO‘SHILADI
    if user_id == ADMIN_ID:
        kb.row(
            KeyboardButton("✏️ Test yaratish")
        )

    return kb
