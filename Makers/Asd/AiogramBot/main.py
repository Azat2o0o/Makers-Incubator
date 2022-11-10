import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5407839692:AAHDvyBhgN3ZZ7O56Abe7f02FbiDSJ5xurs'
ADMIN_ID = '878552645'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_hundler (message: types: Message)
async def send_message ():
    message.reply_to_message('Здравствуйте')

