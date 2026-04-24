from aiogram import types
from main import dp
from bot.config import ADMIN_ID


# =========================
# 📊 NATIJA
# =========================
@dp.message_handler(text="📊 Mening natijalarim")
async def results(message: types.Message):
    await message.answer("📊 Natijalar test yakunlangach chiqadi")


# =========================
# 👤 PROFIL
# =========================
@dp.message_handler(text="👤 Profil")
async def profile(message: types.Message):
    await message.answer("👤 Profil bo‘limi (keyin qo‘shiladi)")


# =========================
# ℹ️ BOT HAQIDA
# =========================
@dp.message_handler(text="ℹ️ Bot haqida")
async def about(message: types.Message):
    await message.answer("📘 Bu bot milliy sertifikat testlari uchun")


# =========================
# ✏️ ADMIN (FAKAT TEKSHIRUV)
# =========================
@dp.message_handler(text="✏️ Test yaratish")
async def create_test(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("✏️ Test yaratish uchun tugmadan foydalaning")
