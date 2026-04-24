from aiogram import types
from main import dp


@dp.message_handler(text="📤 Javob yuborish")
async def send_answers(message: types.Message):
    await message.answer("✍️ Test kodini kiriting:")


@dp.message_handler(text="📊 Mening natijalarim")
async def results(message: types.Message):
    await message.answer("📊 Sizning natijalaringiz hali mavjud emas.")


@dp.message_handler(text="👤 Profil")
async def profile(message: types.Message):
    await message.answer("👤 Profil bo‘limi (hozircha bo‘sh)")


@dp.message_handler(text="ℹ️ Bot haqida")
async def about(message: types.Message):
    await message.answer("📘 Bu bot milliy sertifikat testlari uchun mo‘ljallangan.")
