import aiosqlite


async def new_user(users_id, balance, total_payments):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        insert_query = '''INSERT INTO users (id, balance, total_payments)
                            VALUES (?, ?, ?);'''
        data_tuple = (users_id, balance, total_payments)
        await db.execute(insert_query, data_tuple)
        await db.commit()
        print('Запись успешно добавлена.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        await db.close()


async def check_worker_in_database(user_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        cursor = await db.execute("SELECT EXISTS(SELECT 1 FROM users WHERE id = ?);", (user_id,))
        result = await cursor.fetchone()
        return True if result[0] else False

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
        return "ошибка"
    finally:
        await db.close()
        

async def get_user(user_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        select_query = '''SELECT * FROM users WHERE id = ?;'''
        data_tuple = (user_id,)
        cursor = await db.execute(select_query, data_tuple)
        user_data = await cursor.fetchone()
        await cursor.close()
        if user_data:
            return user_data
        else:
            print('Пользователь с таким ID не найден.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()


async def update_ltc(user_id, new_wallet_value):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        update_query = '''UPDATE users SET ltc = ? WHERE id = ?;'''
        data_tuple = (new_wallet_value, user_id)
        await db.execute(update_query, data_tuple)
        await db.commit()
        print('Значение кошелька успешно обновлено.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()


async def update_btc(user_id, new_wallet_value):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        update_query = '''UPDATE users SET btc = ? WHERE id = ?;'''
        data_tuple = (new_wallet_value, user_id)
        await db.execute(update_query, data_tuple)
        await db.commit()
        print('Значение кошелька успешно обновлено.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()


async def add_to_balance(user_id, amount_to_add):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        # Получаем текущий баланс пользователя
        select_query = '''SELECT balance FROM users WHERE id = ?;'''
        cursor = await db.execute(select_query, (user_id,))
        result = await cursor.fetchone()

        if result is None:
            print(f"Пользователь с ID {user_id} не найден.")
            return

        current_balance = result[0]
        new_balance = float(current_balance) + float(amount_to_add)

        # Обновляем баланс пользователя
        update_query = '''UPDATE users SET balance = ? WHERE id = ?;'''
        data_tuple = (new_balance, user_id)
        await db.execute(update_query, data_tuple)
        await db.commit()
        print('Баланс успешно обновлен.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()


async def add_to_total_balance(user_id, amount_to_add):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        # Получаем текущий баланс пользователя
        select_query = '''SELECT total_payments FROM users WHERE id = ?;'''
        cursor = await db.execute(select_query, (user_id,))
        result = await cursor.fetchone()

        if result is None:
            print(f"Пользователь с ID {user_id} не найден.")
            return

        current_balance = result[0]
        new_balance = float(current_balance) + float(amount_to_add)

        # Обновляем баланс пользователя
        update_query = '''UPDATE users SET total_payments = ? WHERE id = ?;'''
        data_tuple = (new_balance, user_id)
        await db.execute(update_query, data_tuple)
        await db.commit()
        print('Баланс успешно обновлен.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()