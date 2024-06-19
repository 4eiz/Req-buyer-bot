from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u, requests as r
from config import ADMIN, bot

router = Router()



@router.message(Command('payout'))
async def start(message: Message, command: CommandObject):
    id = message.from_user.id
    if id == ADMIN:
        try:
            args = command.args.split()
            if len(args) != 3:
                raise ValueError("Неверное количество аргументов")
            request_id, payout_amount, line_count = map(int, args)

            user_id = await r.get_user_id_by_request_id(request_id=request_id)
            await u.add_to_balance(user_id=user_id, amount_to_add=payout_amount)
            await u.add_to_total_balance(user_id=user_id, amount_to_add=payout_amount)
            await r.delete_req(id=request_id)

            text = f'<b>💸 <code>#{request_id}</code> Сумма к выплате: <code>{payout_amount}$</code> | Колл-во нужных строк: <code>{line_count}</code></b>'
            await bot.send_message(chat_id=user_id, text=text)
            
        except ValueError as e:
            text = f"⚠️ Неверное количество аргументов!\nПроверьте тот ли айди выплаты вы указали!"

    text = f'✅ Выплата произведена успешно!\n{text}'
    await message.answer(text=text)