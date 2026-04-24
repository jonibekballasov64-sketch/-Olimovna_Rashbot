import json
from aiogram import types
from main import dp
from bot.config import ADMIN_ID

# 🔹 WEBAPP LINK (o'zingiznikiga almashtirasiz)
WEBAPP_SOLVE = "https://YOUR-APP.up.railway.app/solve"


# 🔥 1. O‘QUVCHI "Javob yuborish" BOSADI → WEBAPP OCHILADI
@dp.message_handler(text="📤 Javob yuborish")
async def solve_test(message: types.Message):

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        types.KeyboardButton(
            text="✍️ Test ishlash",
            web_app=types.WebAppInfo(url=WEBAPP_SOLVE)
        )
    )

    await message.answer("Testni ishlash uchun bosing 👇", reply_markup=kb)


# 🔥 2. WEBAPP DAN NATIJA KELADI
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def result_handler(message: types.Message):

    try:
        data = json.loads(message.web_app_data.data)
    except:
        await message.answer("❌ Xatolik yuz berdi")
        return

    correct = data.get("correct", 0)
    wrong = data.get("wrong", 0)
    esse = data.get("esse", 0)

    # 🔹 O‘QUVCHIGA XABAR
    await message.answer(
        f"""✅ Javoblaringiz qabul qilindi!

📊 Siz 44 savoldan {correct} tasini to‘g‘ri ishladingiz
❌ Xatolar soni: {wrong}
📝 Esse bali: {esse}

📢 Yakuniy natijalar test yakunlangach e’lon qilinadi"""
    )

    # 🔹 ADMINGA XABAR (sizga keladi)
    await message.bot.send_message(
        ADMIN_ID,
        f"""✅ Testga javoblar qabul qilindi!
👤 Test topshiruvchi: {message.from_user.full_name}

📊 To‘g‘ri: {correct}
❌ Xato: {wrong}
📝 Esse: {esse}

Natijalarni ko‘rish: /natijalar
Testni yakunlash: /yakunlash"""
    )
