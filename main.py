import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import requests
from bs4 import BeautifulSoup
from random import choice
from heandlers.channal import channal_router



load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
CHANNAL_ID = -1002590689329

dp = Dispatcher()
dp.include_router(channal_router)

async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    bot = Bot(token=TOKEN)
    logger.info("Бот создан")
    
    logger.info("Диспетчер создан")

    
    @dp.message(Command("start"))
    async def send_welcome(message: types.Message):
        await message.answer("Бот запущен! Он будет отправлять анекдоты!")
        logger.info("Бот запущен")


    # @dp.message()
    # async def echo(message: types.Message):
    #     await message.answer(message.text)


    @dp.message(Command("anekdot"))
    async def send_welcome(message: types.Message):
        while True:
            try:
                response = requests.get('https://www.anekdot.ru/random/anekdot/')
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jokes = soup.find_all('div', class_='text')

                    random_joke = choice(jokes).text.strip()
                    anekdot = random_joke
                else:
                    anekdot = "Не удалось получить анекдот"

                await bot.send_message(f"Анекдот: {anekdot}")
                logger.info(f"Опублекован анекдот: {anekdot}")
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения {e}")

    

    try:
        await dp.start_polling(bot)
    finally:
        task.cancel()
        await bot.session.close()
        logger.info("Бот остановлен")




if __name__ == '__main__':
    asyncio.run(main())