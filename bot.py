import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from config import BOT_TOKEN

#
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#/start
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\nЯ — шаблон Telegram-бота.")

#/help
@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("🧾 Доступные команды:\n/start — начало\n/help — помощь")

#
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")


#
async def main():
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
