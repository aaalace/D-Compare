import sqlite3

con = sqlite3.connect("database/main_db.sqlite")
cur = con.cursor()


# функция отвечающая за проверку на наличие данного пользователя в БД
def check_user_in_system(username, password):
    global user, pas
    if username == 0 and password == 0:
        return user, pas
    data = cur.execute("""SELECT id FROM users WHERE username = ? AND password = ?""",
                       (str(username), str(password))).fetchall()
    user = username
    pas = password
    if len(data) == 0:
        return False
    return True


# функция отвечающая за изменение пароля
def update_password(new, username):
    if bool(new):
        cur.execute("""UPDATE users
                        SET password = ?
                        WHERE username = ?""", (new, username)).fetchall()
        con.commit()
        return new
    else:
        return 'ОШИБКА'


# добавление нового пользователя в БД с проверкой на условия данных
def register_new_user(username, password):
    us = cur.execute("""SELECT * FROM users""").fetchall()
    if not bool(username) or not bool(password):
        return [False, 'Оба поля не должны быть пустыми']
    cur.execute("""INSERT INTO users VALUES(?, ?, ?)""",
                (len(us) + 1, str(username), str(password))).fetchall()
    con.commit()
    return [True, 0]


# функция отвечающая за получение определенного набора гаджетов для главной страницы
def get_gadgets(param):
    if param[0] == 'all':
        gadgets = cur.execute("""SELECT * FROM gadgets""").fetchall()
        return gadgets
    if param[0] == 'search':
        param = param[1]
        par = f'%{param}%'
        gadgets = cur.execute("""SELECT * FROM gadgets
                                    WHERE name LIKE ?""", (par, )).fetchall()
        return gadgets
    if param[0] == 'filter':
        characteristics = cur.execute("""SELECT id, characteristic FROM gadgets""").fetchall()
        param = param[1]
        indexes = []
        for index, info in characteristics:
            info = info.split(';')
            count = 0

            if float(param[0][1]) >= float(info[0]) >= float(param[0][0]):
                count += 1

            if info[1] == param[1] or param[1] == 'Все':
                count += 1

            if '-' in param[2]:
                mx = param[2].split('-')[1]
                mn = param[2].split('-')[0]
                if float(mx) >= float(info[2]) >= float(mn):
                    count += 1
            if '-' not in param[2]:
                if param[2] == 'Все':
                    count += 1
                else:
                    if eval(f'{info[2]}{param[2]}'):
                        count += 1

            param[3] = param[3].split(' ')[0]
            if '-' in param[3]:
                mx = param[3].split('-')[1]
                mn = param[3].split('-')[0]
                if float(mx) >= float(info[3]) >= float(mn):
                    count += 1
            if '-' not in param[3]:
                if param[3] == 'Все':
                    count += 1
                else:
                    if eval(f'{info[3]}{param[3]}'):
                        count += 1

            param[4] = param[4].split(' ')[0]
            if '=' in param[4]:
                if eval(f'{info[4]}{param[4]}'):
                    count += 1
            if '=' not in param[4]:
                if info[4] == param[4] or param[4] == 'Все':
                    count += 1

            param[5] = param[5].split(' ')[0]
            if '-' in param[5]:
                mx = param[5].split('-')[1]
                mn = param[5].split('-')[0]
                if float(mx) >= float(info[5]) >= float(mn):
                    count += 1
            if '-' not in param[5]:
                if param[5] == 'Все':
                    count += 1
                else:
                    if eval(f'{info[5]}{param[5]}'):
                        count += 1

            param[6] = param[6].split(' ')[0]
            if '-' in param[6]:
                mx = param[6].split('-')[1]
                mn = param[6].split('-')[0]
                if float(mx) >= float(info[6]) >= float(mn):
                    count += 1
            if '-' not in param[6]:
                if param[6] == 'Все':
                    count += 1
                else:
                    if eval(f'{info[6]}{param[6]}'):
                        count += 1

            if info[7] == param[7] or param[7] == 'Все':
                count += 1

            if count == 8:
                indexes.append(index)

        gadgets = []
        for el in indexes:
            gadget = cur.execute("""SELECT * FROM gadgets WHERE id = ?""", (el, )).fetchall()
            gadgets.append(gadget[0])
        return gadgets


# функция отвечающая за сбор информации об устройстве из базы данных
def get_info_for_basket(ind):
    data = cur.execute("""SELECT characteristic FROM gadgets WHERE id = ?""",
                       (ind, )).fetchall()
    name = cur.execute("""SELECT name FROM gadgets WHERE id = ?""",
                       (ind, )).fetchall()
    return name[0][0], data[0][0].split(';')


# функция отвечающая за сбор обзоров из базы данных
def get_reviews_by_button(index):
    info = cur.execute("""SELECT info FROM reviews WHERE id = ?""",
                       (index,)).fetchall()
    review = cur.execute("""SELECT name FROM reviews WHERE id = ?""",
                       (index,)).fetchall()
    return review[0][0], info[0][0].split(';')


def get_reviews():
    reviews = cur.execute("""SELECT * FROM reviews""").fetchall()
    return reviews
