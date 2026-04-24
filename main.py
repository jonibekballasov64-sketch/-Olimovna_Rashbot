from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.config import TOKEN

bot = Bot(token=TOKEN)

storage = MemoryStorage()   # 🔥 SHU QO‘SHILDI
dp = Dispatcher(bot, storage=storage)

from bot.handlers import start, subscription, menu, test_create  # 🔥 create ham qo‘shildi

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    executor.start_polling(dp, skip_updates=True)
