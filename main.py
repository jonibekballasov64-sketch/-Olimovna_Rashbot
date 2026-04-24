from aiogram import Bot, Dispatcher, executor
from bot.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# HANDLERLARNI ULAYMIZ
from bot.handlers import start, subscription, menu

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    executor.start_polling(dp, skip_updates=True)
