from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from keyboards.inline.main_menu import main_menu_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}',reply_markup=main_menu_keyboard)
