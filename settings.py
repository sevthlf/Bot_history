token = "5473196991:AAFLgAsmyxyvtE8KOhf7BSCG_xIIZpya3_0"


# Кнопочки
# from aiogram import Bot, Dispatcher, types
# import asyncio
# from settings import token
#
# bot = Bot(token=token)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=["start"])
# async def cmd_start(message: types.Message):
#    await message.answer("Hello!")
#
# @dp.message_handler(commands=["bye", 'пока', 'au_revoir'])
# async def cmd_bye(message: types.Message):
#    await message.answer("Bye Bye")
#
# @dp.message_handler(commands=["help"])
# async def cmd_help(message: types.Message):
#     await message.reply('Я знаю команды\n/start\n/au_revoir\n/lunch')
#
# @dp.message_handler(commands=["lunch"])
# async def cmd_lunch(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="С пюрешкой")],
#         [types.KeyboardButton(text="С макарошками")],
#         [types.KeyboardButton(text="Без пюрешки")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите способ подачи"
#     )
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

