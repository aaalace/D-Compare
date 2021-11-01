import sqlite3

con = sqlite3.connect("database/main_db.sqlite")
cur = con.cursor()


# проверка на наличие данного пользователя в БД
def check_user_in_system(username, password):
    data = cur.execute("""SELECT id FROM users WHERE username = ? AND password = ?""",
                       (str(username), str(password))).fetchall()
    if len(data) == 0:
        return False
    return True


# добавление нового пользователя в БД с проверкой на условия данных
def register_new_user(username, password):
    us = cur.execute("""SELECT * FROM users""").fetchall()
    if not bool(username) or not bool(password):
        return [False, 'Оба поля не должны быть пустыми']
    cur.execute("""INSERT INTO users VALUES(?, ?, ?)""",
                (len(us) + 1, str(username), str(password))).fetchall()
    con.commit()
    return [True, 0]


def get_gadgets(param):
    if param[0] == 'all':
        gadgets = cur.execute("""SELECT * FROM gadgets""").fetchall()
        return gadgets
    if param[0] == 'search':
        par = f'%{param[1]}%'
        gadgets = cur.execute("""SELECT * FROM gadgets
                                    WHERE name LIKE ?""", (par, )).fetchall()
        return gadgets
    if param[0] == 'filter':
        pass


def get_info_for_basket(ind):
    data = cur.execute("""SELECT characteristic FROM gadgets WHERE id = ?""",
                       (ind, )).fetchall()
    name = cur.execute("""SELECT name FROM gadgets WHERE id = ?""",
                       (ind, )).fetchall()
    return name[0][0], data[0][0].split(';')