from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.types import Message

from keyboards.inline.main_menu import main_menu_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}', reply_markup=main_menu_keyboard)


@dp.message_handler(CommandHelp())
async def bot_help(message: Message):
    await message.answer(f'Полезный бот')
    await message.answer(f'Выберите действие', reply_markup=main_menu_keyboard)
