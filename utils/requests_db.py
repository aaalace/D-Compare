import psycopg2

con = psycopg2.connect(user='postgres',
                      password='Damir1978',
                      host='127.0.0.1',
                      database='postgres')
cur = con.cursor()


# функция отвечающая за проверку на наличие данного пользователя в БД
def check_user_in_system(username, password):
    global user, pas
    if username == 0 and password == 0:
        return user, pas
    cur.execute(f"""SELECT * from users WHERE username = '{username}' AND password = '{password}'""")
    data = cur.fetchall()
    user = username
    pas = password
    if len(data) == 0:
        return False
    return True


# функция отвечающая за изменение пароля
def update_password(new, username):
    if bool(new):
        cur.execute(f"""UPDATE users
                        SET password = '{new}'
                        WHERE username = '{username}'""")
        con.commit()
        return new
    else:
        return 'ОШИБКА'


# добавление нового пользователя в БД с проверкой на условия данных
def register_new_user(username, password):
    cur.execute("""SELECT * FROM users""")
    us = cur.fetchall()
    if not bool(username) or not bool(password):
        return [False, 'Оба поля не должны быть пустыми']
    cur.execute(f"""INSERT INTO users 
                    VALUES ({len(us) + 1}, '{username}', '{password}')""")
    con.commit()
    return [True, 0]


# функция отвечающая за получение определенного набора гаджетов для главной страницы
def get_gadgets(param):
    if param[0] == 'all':
        us = cur.execute("""SELECT * FROM gadgets""")
        gadgets = cur.fetchall()
        return gadgets
    if param[0] == 'search':
        param = param[1]
        sql = f"SELECT * FROM gadgets WHERE name LIKE '%{param.capitalize()}%'"
        cur.execute(sql)
        gadgets = cur.fetchall()
        return gadgets
    if param[0] == 'filter':
        cur.execute("""SELECT gadget_id, characteristic FROM gadgets""")
        characteristics = cur.fetchall()
        param = param[1]
        indexes = []
        for index, info in characteristics:
            info = info.split(';')
            count = 0

            try:
                if float(param[0][1]) >= float(info[0]) >= float(param[0][0]):
                    count += 1
            except ValueError:
                pass

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
            cur.execute(f"""SELECT * FROM gadgets WHERE gadget_id = {el}""")
            gadget = cur.fetchall()
            gadgets.append(gadget[0])
        return gadgets


# функция отвечающая за сбор информации об устройстве из базы данных
def get_info_for_basket(ind):
    cur.execute(f"""SELECT characteristic FROM gadgets WHERE gadget_id = {ind}""")
    data = cur.fetchall()
    cur.execute(f"""SELECT name FROM gadgets WHERE gadget_id = {ind}""")
    name = cur.fetchall()
    return name[0][0], data[0][0].split(';')


# функция отвечающая за сбор обзоров из базы данных
def get_reviews_by_button(index):
    cur.execute(f"""SELECT info FROM reviews WHERE review_id = {index}""")
    info = cur.fetchall()
    cur.execute(f"""SELECT name FROM reviews WHERE review_id = {index}""")
    review = cur.fetchall()
    return review[0][0], info[0][0].split(';')


def get_readmore_by_button(index):
    cur.execute(f"""SELECT url FROM gadgets WHERE gadget_id = {index}""")
    data = cur.fetchall()
    cur.execute(f"""SELECT name FROM gadgets WHERE gadget_id = {index}""")
    name = cur.fetchall()
    return name[0][0], data[0][0]


def get_reviews():
    cur.execute("""SELECT * FROM reviews""")
    reviews = cur.fetchall()
    return reviews


def get_pic_gadgets():
    cur.execute("""SELECT picture FROM gadgets WHERE gadget_id = 1""")
    pic = cur.fetchall()
    return pic[0][0]