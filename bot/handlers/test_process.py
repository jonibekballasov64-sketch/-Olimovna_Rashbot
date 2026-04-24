import json
from aiogram import types
from main import dp
from bot.config import ADMIN_ID

from bot.handlers.test_create import TESTS
from bot.utils.checker import check_all
from bot.utils.rash import estimate_theta, theta_to_test_ball

RESULTS = []

WEBAPP_SOLVE = "https://YOUR-APP.up.railway.app/solve"


@dp.message_handler(text="📤 Javob yuborish")
async def solve_test(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(
        text="✍️ Test ishlash",
        web_app=types.WebAppInfo(url=WEBAPP_SOLVE)
    ))
    await message.answer("👇 Testni boshlash", reply_markup=kb)


@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def result_handler(message: types.Message):

    try:
        data = json.loads(message.web_app_data.data)
    except:
        await message.answer("❌ Xatolik")
        return

    code = data.get("code")
    answers = data.get("answers", {})
    esse = int(data.get("esse", 0))

    if code not in TESTS:
        await message.answer("❌ Test kodi noto‘g‘ri")
        return

    correct_answers = TESTS[code]

    # 🔥 TEKSHIRUV (TO‘G‘RI FUNKSIYA)
    responses, correct, wrong_count, wrong_list = check_all(answers, correct_answers)

    # 🔥 RASCH
    theta = estimate_theta(responses)
    test_ball = theta_to_test_ball(theta)

    # 🔥 YAKUNIY
    final = round((test_ball + esse) / 2, 1)

    if final >= 70: grade = "A+"
    elif final >= 65: grade = "A"
    elif final >= 60: grade = "B+"
    elif final >= 55: grade = "B"
    elif final >= 50: grade = "C+"
    elif final >= 46: grade = "C"
    else: grade = "Fail"

    # 🔥 SAQLASH (MUHIM)
    RESULTS.append({
        "user_id": message.from_user.id,
        "name": message.from_user.full_name,
        "correct": correct,
        "wrong": wrong_count,
        "wrong_list": wrong_list,
        "esse": esse,
        "test_ball": test_ball,
        "final": final,
        "grade": grade
    })

    # 🔹 O‘QUVCHI (hozir qisqa)
    await message.answer(
        f"""✅ Javoblaringiz qabul qilindi!

📊 Siz 44 savoldan {correct} tasini to‘g‘ri ishladingiz
📝 Esse bali: {esse}

📢 Yakuniy natijalar test yakunlangach e’lon qilinadi"""
    )

    # 🔹 ADMIN
    await message.bot.send_message(
        ADMIN_ID,
        f"""✅ Testga javoblar qabul qilindi!
👤 {message.from_user.full_name}

📊 To‘g‘ri: {correct} / 44
📝 Esse: {esse}

👉 /natijalar
👉 /yakunlash"""
    )
