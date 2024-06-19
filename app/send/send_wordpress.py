import os

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from keyboards import client as k
from data import users as u, requests as r
from config import bot, ADMIN_CHANNEL_ID

class WordPress(StatesGroup):
    file = State()

router = Router()



@router.callback_query(k.Menu_callback.filter(F.menu == 'send_wordpress'))
async def send_wordpress(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):
    await state.set_state(WordPress.file)
    text = '''<b>Отправляй строки одним файлом .txt в формате URL:LOGIN:PASSWORD или LOGIN:PASSWORD:URL.
Разделитель : или ;. В других случаях обращайся в поддержку.
Запросы:
<code>wp-admin
wp-login
wc-login</code></b>'''
    await call.message.edit_text(text=text, reply_markup=k.cancel())


@router.message(WordPress.file, F.document)
async def handle_file(message: Message, state: FSMContext):
    document = message.document
    file_info = await bot.get_file(document.file_id)
    file_path = f"temp/{document.file_name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    await bot.download_file(file_info.file_path, destination=file_path)

    file = FSInputFile(path=file_path, filename='wordpress.txt')

    target_channel_id = ADMIN_CHANNEL_ID

    tg_tag = message.from_user.username
    user_id = message.from_user.id
    request = await r.new_request(users_id=user_id)
    data = await u.get_user(user_id=user_id)
    ltc = data[3]
    btc = data[4]

    text = f'''<b>🔢 REQUEST_ID = <code>{request}</code>
👻 TG: @{tg_tag}
👻 USER_ID: <code>{user_id}</code>

🔷 LTC: <code>{ltc}</code>
🔶 BTC: <code>{btc}</code></b>'''
    await bot.send_document(chat_id=target_channel_id, document=file, caption=text)
    

    text = "<b>Файл успешно обработан и отправлен.</b>"
    await message.answer(text=text)
    
    
    await state.clear()
    os.remove(file_path)