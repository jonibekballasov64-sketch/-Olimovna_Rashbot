from aiogram import types
from main import dp
from bot.keyboards.reply import menu_keyboard


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):

    # 🔥 ID NI KO‘RISH (tekshiruv uchun)
    await message.answer(f"ID: {message.from_user.id}")

    # ✅ ASOSIY MENYU
    await message.answer(
        "🎓 Milliy Sertifikat botiga xush kelibsiz!\n\nKerakli bo‘limni tanlang 👇",
        reply_markup=menu_keyboard(message.from_user.id)
    )
