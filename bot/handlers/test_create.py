from aiogram import types
from main import dp
from bot.config import ADMIN_ID

WEBAPP_URL = "https://YOUR-URL.up.railway.app"

@dp.message_handler(text="✏️ Test yaratish")
async def create_test(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        types.KeyboardButton(
            text="📝 Test yaratish",
            web_app=types.WebAppInfo(url=WEBAPP_URL)
        )
    )

    await message.answer("Test yaratish tugmasini bosing 👇", reply_markup=kb)
