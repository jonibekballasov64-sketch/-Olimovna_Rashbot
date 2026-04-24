from aiogram import types
from main import dp
from bot.config import ADMIN_ID

WEBAPP_CREATE = "https://YOUR-APP.up.railway.app/create"

@dp.message_handler(text="✏️ Test yaratish")
async def create_test(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(
        text="📝 Forma ochish",
        web_app=types.WebAppInfo(url=WEBAPP_CREATE)
    ))

    await message.answer("Test yaratish uchun bosing 👇", reply_markup=kb)
