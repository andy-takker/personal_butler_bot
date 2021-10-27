from aiogram import executor, Dispatcher
from loader import dp, bot
from utils import on_startup_notify
from utils.commands import set_default_commands

import middlewares
import handlers

async def on_startup(dispatcher: Dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher: Dispatcher):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
