from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.config import TOKEN

bot = Bot(token=TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# 🔥 HAMMA HANDLERLAR
from bot.handlers import (
    start,
    subscription,
    menu,
    test_create,
    test_process,
    results,
    finish
)

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    executor.start_polling(dp, skip_updates=True)
