from aiogram import types
from main import dp
from bot.config import ADMIN_ID

WEBAPP_SOLVE = "https://YOUR-APP.up.railway.app/solve"
WEBAPP_CREATE = "https://YOUR-APP.up.railway.app/"

# =========================
# 📤 JAVOB YUBORISH (WEBAPP)
# =========================
@dp.message_handler(text="📤 Javob yuborish")
async def send_answers(message: types.Message):

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(types.KeyboardButton(
        text="✍️ Test ishlash",
        web_app=types.WebAppInfo(url=WEBAPP_SOLVE)
    ))

    await message.answer("👇 Testni boshlash", reply_markup=kb)


# =========================
# ✏️ TEST YARATISH (ADMIN)
# =========================
@dp.message_handler(text="✏️ Test yaratish")
async def create_test(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(types.KeyboardButton(
        text="📝 Test yaratish",
        web_app=types.WebAppInfo(url=WEBAPP_CREATE)
    ))

    await message.answer("👇 Test yaratish sahifasi", reply_markup=kb)


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
