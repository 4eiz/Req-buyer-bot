from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

API_TOKEN = '' # Токен бота

ADMIN = 6923427988 # Айди админа
ADMIN_CHANNEL_ID = -4133308346 # Айди чата, куда будут приходить заявки
ADMIN_NAME = '@wpxenjoyer' # Юзернейм саппорта

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))