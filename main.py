import logging
from settings import token
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


# webhook settings
WEBHOOK_HOST = 'https://c473-188-243-183-222.eu.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 8000

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message('Привет!')

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await bot.send_message('Ты обратился к справке бота')

async def on_startup(dp):
   await bot.set_webhook(WEBHOOK_URL)
   # insert code here to run it after start


async def on_shutdown(dp):
   logging.warning('Shutting down..')

   # insert code here to run it before shutdown

   # Remove webhook (not acceptable in some cases)
   await bot.delete_webhook()

   # Close DB connection (if used)
   await dp.storage.close()
   await dp.storage.wait_closed()

   logging.warning('Bye!')


if __name__ == '__main__':
   start_webhook(
       dispatcher=dp,
       webhook_path=WEBHOOK_PATH,
       on_startup=on_startup,
       on_shutdown=on_shutdown,
       skip_updates=True,
       host=WEBAPP_HOST,
       port=WEBAPP_PORT,
   )