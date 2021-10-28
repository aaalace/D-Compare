import sqlite3

con = sqlite3.connect("databases/main_db.sqlite")
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
        return [False, 'Оба поля должны быть заполнены']
    elif len(username) < 3 or len(password) < 3:
        return [False, 'Длина логина и пароля должна быть не меньше 3 символов']
    cur.execute("""INSERT INTO users VALUES(?, ?, ?)""",
                (len(us) + 1, str(username), str(password))).fetchall()
    return [True, 0]
