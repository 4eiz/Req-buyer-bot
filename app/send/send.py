from aiogram import Router
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users


router = Router()



@router.callback_query(k.Menu_callback.filter(F.menu == 'send_strings'))
async def user_profil(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):
    try:
        await state.clear()
    except:
        pass
    
    text = '<b>Что будешь отправлять?</b>'
    kb = k.send_something()

    await call.message.edit_text(text=text, reply_markup=kb)