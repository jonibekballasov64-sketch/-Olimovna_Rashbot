from aiogram import types
from main import dp

WEBAPP_SOLVE = "https://YOUR-APP.up.railway.app/solve"

@dp.message_handler(text="📤 Javob yuborish")
async def solve_test(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(
        text="✍️ Test ishlash",
        web_app=types.WebAppInfo(url=WEBAPP_SOLVE)
    ))

    await message.answer("Testni ishlash uchun bosing 👇", reply_markup=kb)
