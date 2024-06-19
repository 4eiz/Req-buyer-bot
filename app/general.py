from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users


router = Router()




@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    try:
        await state.clear()
    except:
        pass

    id = message.from_user.id
    start_user = await users.check_worker_in_database(id)

    if start_user == False:
        await users.new_user(users_id=id, balance=0, total_payments=0)

    text = f'''<b>Привет👋, <code>{message.from_user.first_name}</code>!
Ты попал в бота по скупке запросов.

💲 В профиле необходимо привязать кошельки для выплат
⌛️ Чек занимает от часа до двух суток</b>'''
    kb = k.menu()

    await message.answer(text=text, reply_markup=kb)



@router.callback_query(k.Menu_callback.filter(F.menu == 'menu'))
async def start(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):
    try:
        await state.clear()
    except:
        pass

    text = f'''<b>Привет👋, <code>{call.from_user.first_name}</code>!
Ты попал в бота по скупке запросов.

💲 В профиле необходимо привязать кошельки для выплат
⌛️ Чек занимает от часа до двух суток</b>'''
    kb = k.menu()

    await call.message.edit_text(text=text, reply_markup=kb)