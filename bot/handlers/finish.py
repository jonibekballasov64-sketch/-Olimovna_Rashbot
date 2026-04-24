from aiogram import types
from main import dp, bot
from bot.config import ADMIN_ID

from bot.handlers.test_process import RESULTS
from bot.utils.pdf import create_final_pdf


@dp.message_handler(commands=["yakunlash"])
async def finish_test(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    if not RESULTS:
        await message.answer("❌ Hali natijalar yo‘q")
        return

    filename = "natijalar.pdf"

    create_final_pdf(RESULTS, filename)

    # 🔹 Sizga PDF
    await message.answer_document(open(filename, "rb"))

    # 🔥 O‘QUVCHILARGA AVTO YUBORISH
    for r in RESULTS:
        try:
            wrongs = ", ".join(map(str, r["wrong_list"])) if r["wrong_list"] else "yo‘q"

            await bot.send_message(
                r["user_id"],
                f"""📊 Test yakunlandi!

❌ Xatolaringiz: {wrongs}

📝 Esse: {r['esse']}
📈 Yakuniy natija: {r['final']}
🎓 Daraja: {r['grade']}"""
            )
        except:
            pass  # user bloklagan bo‘lishi mumkin

    await message.answer("✅ Test yakunlandi!")

    # 🔥 xohlasangiz tozalash
    # RESULTS.clear()
