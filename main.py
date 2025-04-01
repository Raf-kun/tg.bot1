import os
import asyncio

from dotenv import load_dotenv, find_dotenv
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import requests
from bs4 import BeautifulSoup
from random import choice

from heandlers.user_private import setup_private_heandlers
from heandlers.channal import setup_channel_heandlers


dp = Dispatcher()


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
CHANNAL_ID = -1002590689329


async def main() -> None:
    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}',
               rotation='3 days',
               backtrace=True,
               diagnose=True)
    bot = Bot(token=os.getenv('TOKEN'))
    setup_private_heandlers(dp)
    setup_channel_heandlers(dp, bot)

    await bot.delete_webhook(drop_pending_updates=True)
    # async def send_random_joke():
    #     while True:
    #         try:
    #             response = requests.get('https://www.anekdot.ru/random/anekdot/')
    #             if response.status_code == 200:
    #                 soup = BeautifulSoup(response.text, 'html.parser')
    #                 jokes = soup.find_all('div', class_='text')

    #                 random_joke = choice(jokes).text.strip()
    #                 anekdot = random_joke
    #             else:
    #                 anekdot = "Не удалось получить анекдот"

    #             await bot.send_message(CHANNEL_ID, f"Анекдот: {anekdot}")
    #             logger.info(f"Опублекован анекдот: {anekdot}")
    #         except Exception as e:
    #             logger.error(f"Ошибка при отправке сообщения {e}")

    #         await asyncio.sleep(180)

    # task = asyncio.create_task(send_random_joke())

    try:
        await dp.start_polling(bot)
    finally:
        # task.cancel()
        await bot.session.close()
        logger.info("Бот остановлен")





if __name__ == '__main__':
    asyncio.run(main())