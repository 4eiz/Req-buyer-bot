from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from data.users import get_user


class Menu_callback(CallbackData, prefix="menu"):
    menu: str


def menu():
    kb = [
        [
            types.InlineKeyboardButton(text='👻 Профиль', callback_data=Menu_callback(menu="profil").pack()),
        ],
        [
            types.InlineKeyboardButton(text='👹 Поддержка', callback_data=Menu_callback(menu="support").pack()),
        ],
        [
            types.InlineKeyboardButton(text='💸 Отправить строки', callback_data=Menu_callback(menu="send_strings").pack()),
        ],
    ]
    
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def profil():
    kb = [
        [
            types.InlineKeyboardButton(text='💳 Изменить кошелек', callback_data=Menu_callback(menu="change_wallet").pack()),
        ],
        [
            types.InlineKeyboardButton(text='↩️ Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def cancel2():
    kb = [
        [
            types.InlineKeyboardButton(text='↩️ Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def cancel():
    kb = [
        [
            types.InlineKeyboardButton(text='❌ Отмена', callback_data=Menu_callback(menu="send_strings").pack())
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


async def wallets(user_id):
    kb = [
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]


    ltc_change = [types.InlineKeyboardButton(text='🔷 Изменить LTC', callback_data=Menu_callback(menu="change_ltc").pack())]
    ltc_add = [types.InlineKeyboardButton(text='🔷 Привязать LTC', callback_data=Menu_callback(menu="change_ltc").pack())]

    btc_change = [types.InlineKeyboardButton(text='🔶 Изменить BTC', callback_data=Menu_callback(menu="change_btc").pack())]
    btc_add = [types.InlineKeyboardButton(text='🔶 Привязать BTC', callback_data=Menu_callback(menu="change_btc").pack())]

    data = await get_user(user_id=user_id)
    ltc = data[3]
    btc = data[4]


    if btc == None:
        kb = [btc_add] + kb
    else:
        kb = [btc_change] + kb


    if ltc == None:
        kb = [ltc_add] + kb
    else:
        kb = [ltc_change] + kb

    return types.InlineKeyboardMarkup(inline_keyboard=kb)




def send_something():
    kb = [
        [
            types.InlineKeyboardButton(text='Отправить WordPress', callback_data=Menu_callback(menu="send_wordpress").pack())
        ],
        [
            types.InlineKeyboardButton(text='Отправить CMS', callback_data=Menu_callback(menu="send_cms").pack())
        ],
        [
            types.InlineKeyboardButton(text='Отправить агрегаторы', callback_data=Menu_callback(menu="send_aggregators").pack())
        ],
        [
            types.InlineKeyboardButton(text='↩️ Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def send_aggregators():
    kb = [
        [
            types.InlineKeyboardButton(text='Отправить orion.managewp.com', callback_data=Menu_callback(menu="send_managewp").pack())
        ],
        [
            types.InlineKeyboardButton(text='↩️ Назад', callback_data=Menu_callback(menu="send_strings").pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)
