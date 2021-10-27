from aiogram import Dispatcher
from aiogram.types import BotCommand


async def set_default_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands(
        [
            BotCommand('start', 'Запустить бота'),
            BotCommand('help', 'Показать справку'),
            BotCommand('reset', 'Прервать операцию и выйти в основное меню')
        ]
    )