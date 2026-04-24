import json
from aiogram import types
from main import dp
from bot.config import ADMIN_ID

# vaqtinchalik
TESTS = {}

WEBAPP_CREATE = "https://YOUR-APP.up.railway.app/create"


# 🔹 tugma
@dp.message_handler(text="✏️ Test yaratish")
async def create_test(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(
        text="📝 Test yaratish",
        web_app=types.WebAppInfo(url=WEBAPP_CREATE)
    ))

    await message.answer("Test yaratish uchun bosing 👇", reply_markup=kb)


# 🔹 webapp data
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def create_handler(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    data = json.loads(message.web_app_data.data)

    code = data.get("code")
    test = data.get("test")

    TESTS[code] = test

    text = f"""Assalomu alaykum. Berilgan testni ishlang.

🔑 Test kodi: {code}

👉 @Olimovna_Rashbot orqali ishlang
📝 45-savol esse o‘quvchi tomonidan kiritiladi"""

    await message.answer("✅ Test yaratildi!")
    await message.answer(text)
