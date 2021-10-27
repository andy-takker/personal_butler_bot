from environs import Env
import os

env = Env()
env.read_env()

basedir = os.path.abspath((os.path.dirname(__file__)))

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')
ADMINS = env.list('ADMINS')
PASSWORD = env.str('BEELINE_PASSWORD')
PHONE_NUMBER = env.str('BEELINE_PHONE_NUMBER')
