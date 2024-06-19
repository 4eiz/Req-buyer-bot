from aiogram import Router
from aiogram.types import Message
from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import client as k
from data import users
from config import ADMIN_NAME

router = Router()


@router.callback_query(k.Menu_callback.filter(F.menu == 'support'))
async def change_wallet(call: CallbackQuery, callback_data: k.Menu_callback):

    text = f'''<b>🧐 Появились вопросы?
Пиши: {ADMIN_NAME}</b>'''
    
    kb = k.cancel2()

    await call.message.edit_text(text=text, reply_markup=kb)