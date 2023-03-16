from aiogram import Bot, Dispatcher, types
import asyncio
from settings import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
   await message.answer("Hello!")

@dp.message_handler(commands=["bye", 'пока', 'au_revoir'])
async def cmd_bye(message: types.Message):
   await message.answer("Bye Bye")

@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.reply('Я знаю команды\n/start\n/au_revoir')

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
