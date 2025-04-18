from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from loguru import logger
from reply import get_keyboard


def setup_private_heandlers(dp: Dispatcher):
    @dp.message(Command('start'), F.chat.type == "private")
    async def private_start(message: types.Message):
        await message.answer(f"Здравствуйте,\
 {(message.from_user.full_name)},\
 Я могу отправить вам анекдот")
        await message.answer(
        "Привет, я бот-анекдот",
        reply_markup=get_keyboard(
            "Отправить анекдот",
            "О нас",
            placeholder="Отправляй что хочешь!"
        ),
    )


    @dp.message(F.chat.type == "private")
    async def private_echo(message: types.Message):
        await message.answer(f"Вы написали в ЛС: {message.text}")
        logger.info(f"ЛС: эхо для {message.from_user.id}")
