import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5203534164:AAFHs3QkFr_szIXaeHe0PYKg-FtL5LwHYlY'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom men wikipediadan maqolalarni topishda yordam beraman")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Foydalanish uchun izlayotgan maqolangizga doir so'z yuboring!")


@dp.message_handler()
async def wikiyubor(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.reply('Malumot topilmadi')

    # old style:
    # await bot.send_message(message.chat.id, message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)