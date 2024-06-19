from aiogram import Router
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users


router = Router()



@router.callback_query(k.Menu_callback.filter(F.menu == 'profil'))
async def user_profil(call: CallbackQuery, callback_data: k.Menu_callback):

    id = call.from_user.id
    data = await users.get_user(user_id=id)
    # print(data)
    user_id = data[0]
    tg_tag = call.from_user.username
    balance = data[1]
    total_payments = data[2]
    ltc = data[3]
    btc = data[4]

    text = f'''<b>👻 ID: {user_id}
👻 TG: @{tg_tag}

Привязанные кошельки:
💲 LTC: <code>{ltc}</code>
💲 BTC: <code>{btc}</code>

💰 Баланс: <code>{balance}$</code>
💰 Общая сумма выплат: <code>{total_payments}$</code></b>'''
    kb = k.profil()

    await call.message.edit_text(text=text, reply_markup=kb)