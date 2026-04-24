from aiogram import Bot, Dispatcher, executor
from bot.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# handlerlarni ulaymiz
from bot.handlers import start, subscription, menu

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
