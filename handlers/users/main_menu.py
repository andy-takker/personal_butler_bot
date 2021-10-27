from aiogram.types import CallbackQuery

import config
from keyboards.inline.main_menu import main_menu_keyboard
from loader import dp
from utils.beeline import BeelineAPI


@dp.callback_query_handler(text_contains='check_balance', state=None)
async def check_balance_button(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.edit_reply_markup(reply_markup=None)
    token = BeelineAPI.get_token(phone_number=config.PHONE_NUMBER, password=config.PASSWORD)
    balance = BeelineAPI.get_balance(phone_number=config.PHONE_NUMBER, token=token)
    await call.message.answer(text=f'Ваш баланс составляет: {round(balance, 2)} руб.')
    await call.message.answer(text='Выберите действие:', reply_markup=main_menu_keyboard)
