from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users

class Btc(StatesGroup):
    new_wallet = State()

router = Router()



@router.callback_query(k.Menu_callback.filter(F.menu == 'change_btc'))
async def change_wallet(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):
    await state.set_state(Btc.new_wallet)
    text = '<b>Введите адрес кошелька:</b>'
    await call.message.edit_text(text=text, reply_markup=k.cancel())


@router.message(Btc.new_wallet)
async def result(message: Message, state: FSMContext):

    user_id = message.from_user.id
    new_adress = message.text

    await users.update_btc(user_id=user_id, new_wallet_value=new_adress)

    text = '<b>Кошёлек успешно изменён!</b>'
    await message.answer(text=text, reply_markup=k.menu())

    await state.clear()