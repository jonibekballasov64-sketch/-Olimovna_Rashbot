from aiogram import types
from main import dp
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

    await message.answer_document(open(filename, "rb"))

    await message.answer("✅ Test yakunlandi!")

    # 🔥 xohlasangiz tozalash
    # RESULTS.clear()
