from aiogram import types
from main import bot, dp
from bot.config import CHANNELS
from bot.keyboards.inline import sub_keyboard
from bot.keyboards.reply import menu_keyboard


# 🔥 OBUNA TEKSHIRUV
async def check_sub(user_id):
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "creator", "administrator"]:
                return False
        except:
            return False
    return True


# 🔥 "A'zo bo‘ldim" BOSILGANDA
@dp.callback_query_handler(lambda c: c.data == "check_sub")
async def check_sub_callback(callback: types.CallbackQuery):

    if await check_sub(callback.from_user.id):
        await callback.message.answer(
            "✅ Obuna tasdiqlandi!",
            reply_markup=menu_keyboard(callback.from_user.id)  # 🔥 MUHIM
        )
    else:
        await callback.answer("❌ Hali obuna bo‘lmagansiz", show_alert=True)
        return

    await callback.answer()  # 🔥 MUHIM
