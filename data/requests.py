import aiosqlite


async def new_request(users_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        insert_query = '''INSERT INTO requests (user_id) VALUES (?);'''
        data_tuple = (users_id,)
        cursor = await db.execute(insert_query, data_tuple)
        await db.commit()
        
        # Получение ID последней вставленной записи
        last_row_id = cursor.lastrowid
        print('Запись успешно добавлена. ID:', last_row_id)

        return last_row_id

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
        return None
    finally:
        await db.close()
    

async def delete_req(id):
    db = await aiosqlite.connect('data/db/base.db')

    try:
        delete_query = "DELETE FROM requests WHERE id=?;"
        await db.execute(delete_query, (id,))
        await db.commit()
        print(f"Запрос {id} успешно удален.")

    except aiosqlite.Error as error:
        print("Не удалось выполнить запрос на удаление данных из таблицы.", error)
    
    finally:
        await db.close()



async def get_user_id_by_request_id(request_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        select_query = '''SELECT user_id FROM requests WHERE id = ?;'''
        cursor = await db.execute(select_query, (request_id,))
        result = await cursor.fetchone()
        
        if result:
            user_id = result[0]
            print('ID пользователя:', user_id)
            return user_id
        else:
            print('Запись не найдена.')
            return None

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
        return None
    finally:
        await db.close()