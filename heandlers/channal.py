import asyncio
from random import choice
from bs4 import BeautifulSoup
from loguru import logger
import requests
from aiogram import Bot, types, Router
from main import bot

channal_router = Router()

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

                await bot.send_message(CHANNAL_ID, f"Анекдот: {anekdot}")
                logger.info(f"Опублекован анекдот: {anekdot}")
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения {e}")

            await asyncio.sleep(60)

task = asyncio.create_task(send_random_joke())
