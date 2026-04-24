from aiogram import types
from main import dp
from bot.handlers.subscription import check_sub
from bot.keyboards.inline import sub_keyboard
from bot.keyboards.reply import menu_keyboard


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):

    if not await check_sub(message.from_user.id):
        await message.answer(
            "🔒 Botdan foydalanish uchun quyidagi kanallarga a'zo bo‘ling:",
            reply_markup=sub_keyboard()
        )
        return

    await message.answer(
        "🎓 Milliy Sertifikat botiga xush kelibsiz!\n\nKerakli bo‘limni tanlang 👇",
        reply_markup=menu_keyboard()
    )
