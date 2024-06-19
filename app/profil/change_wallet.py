from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users


router = Router()




@router.callback_query(k.Menu_callback.filter(F.menu == 'change_wallet'))
async def change_wallet(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    id = call.from_user.id

    text = '<b>Выберите кошёлек который вы хотите привязать/изменить</b>'
    kb = await k.wallets(id)

    await call.message.edit_text(text=text, reply_markup=kb)