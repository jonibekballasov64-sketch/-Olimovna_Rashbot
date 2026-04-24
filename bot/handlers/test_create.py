from aiogram import types
from main import dp
from bot.config import ADMIN_ID
from bot.utils.code_generator import generate_code

# vaqtinchalik xotira (keyin DB qilamiz)
TESTS = {}

# =========================
# ADMIN TEST BOSHLASH
# =========================
@dp.message_handler(commands=["create_test"])
async def create_test_start(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "📝 Test yaratish boshlandi.\n\n"
        "1–32 savollar (A B C D) javoblarini ketma-ket yuboring.\n\n"
        "Masalan:\nABCDABCD..."
    )

    dp.current_state(user=message.from_user.id).set_state("q1_32")


# =========================
# 1–32 JAVOB
# =========================
@dp.message_handler(state="q1_32")
async def get_1_32(message: types.Message):
    answers = message.text.strip().upper()

    if len(answers) != 32:
        await message.answer("❌ 32 ta javob bo‘lishi kerak!")
        return

    dp.current_state(user=message.from_user.id).update_data(q1_32=answers)

    await message.answer("33–35 (A B C D E F) javoblarini yuboring:")
    dp.current_state(user=message.from_user.id).set_state("q33_35")


# =========================
# 33–35 JAVOB
# =========================
@dp.message_handler(state="q33_35")
async def get_33_35(message: types.Message):
    answers = message.text.strip().upper()

    if len(answers) != 3:
        await message.answer("❌ 3 ta javob bo‘lishi kerak!")
        return

    dp.current_state(user=message.from_user.id).update_data(q33_35=answers)

    await message.answer("36–39 savollar (vergul bilan, sinonim ham yozing):\nmasalan: osmon,falak,samo")
    dp.current_state(user=message.from_user.id).set_state("q36_39")


# =========================
# 36–39 (SINONIM)
# =========================
@dp.message_handler(state="q36_39")
async def get_36_39(message: types.Message):
    answers = message.text.lower().split(",")

    dp.current_state(user=message.from_user.id).update_data(q36_39=answers)

    await message.answer("40–44 (A va B juft yozing: masalan: kitob|yozuvchi)")
    dp.current_state(user=message.from_user.id).set_state("q40_44")


# =========================
# 40–44
# =========================
@dp.message_handler(state="q40_44")
async def get_40_44(message: types.Message):
    answers = message.text.lower().split("|")

    dp.current_state(user=message.from_user.id).update_data(q40_44=answers)

    # -------------------------
    # TEST YAKUNI
    # -------------------------
    data = await dp.current_state(user=message.from_user.id).get_data()

    code = generate_code()

    TESTS[code] = data

    text = f"""
Assalomu alaykum. Berilgan testni ishlang va quyidagi qadamlarni ketma-ket bajaring.

🟦 1-qadam: Botga kiring.
🟦 2-qadam: Start → Obuna bo‘lish → Qayta Start.
🟦 3-qadam: Menyu chiqadi. Undan «📤 Javob yuborish» tugmasini bosing.
🟦 4-qadam: Test kodini kiriting.

🔑 Test kodi: {code}

✍️ Javoblaringizni imloviy xatolarsiz kiriting.
📊 Natija test yakunlangach e’lon qilinadi.

👉 Bot manzili: @Olimovna_Rashbot

📝 45-savol (esse) uchun ball o‘qituvchi tomonidan kiritiladi.
"""

    await message.answer("✅ Test yaratildi!\n\n" + text)

    await dp.current_state(user=message.from_user.id).finish()
