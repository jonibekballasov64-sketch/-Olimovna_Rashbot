from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import CHANNELS


def sub_keyboard():
    kb = InlineKeyboardMarkup(row_width=1)

    for ch in CHANNELS:
        kb.add(
            InlineKeyboardButton(
                text=f"📢 {ch}",
                url=f"https://t.me/{ch[1:]}"
            )
        )

    kb.add(
        InlineKeyboardButton(
            text="✅ A'zo bo‘ldim",
            callback_data="check_sub"
        )
    )

    return kb
