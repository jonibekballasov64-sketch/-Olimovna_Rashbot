from aiogram import types
from main import dp
from bot.handlers.test_process import RESULTS


@dp.message_handler(commands=["natijalar"])
async def show_results(message: types.Message):

    if not RESULTS:
        await message.answer("❌ Hali natijalar yo‘q")
        return

    text = "📊 Joriy holat:\n\n"

    for i, r in enumerate(RESULTS, 1):
        text += f"{i}. {r['name']} — {r['correct']}/44\n"

    await message.answer(text)
