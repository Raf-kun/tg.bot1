import asyncio
from random import choice
from bs4 import BeautifulSoup
from loguru import logger
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

CHANNAL_ID = -1002590689329

async def send_random_joke():
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

                await Bot.send_message(CHANNAL_ID, f"Анекдот: {anekdot}")
                logger.info(f"Опублекован анекдот: {anekdot}")
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения {e}")

            await asyncio.sleep(60)

task = asyncio.create_task(send_random_joke())

def setup_channel_heandlers(dp: Dispatcher, bot: Bot):
    asyncio.create_task(send_random_joke(bot))

    @dp.message(Command('channel_stats'), F.chat.type == "channel")
    async def channel_stats(message: types.Message):
        await message.answer("Бот канала работает!")
        logger.info("Канал: проверка работы")