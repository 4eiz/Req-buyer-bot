import asyncio
import logging

from aiogram import Dispatcher

from app import general, support, admin
from app.profil import profil, change_wallet, ltc, btc
from app.send import send, send_wordpress, send_aggregators, send_cms

from config import bot


async def start():   
    dp = Dispatcher()

    dp.include_routers(
        general.router,
        profil.router,
        change_wallet.router,
        ltc.router,
        btc.router,
        support.router,
        send.router,
        send_wordpress.router,
        admin.router,
        send_aggregators.router,
        send_cms.router,
    )

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(start())