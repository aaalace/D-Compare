import sys

from templates.forms.login import Login_Form
from templates.forms.signin import Signin_Form
from templates.forms.main_wind import Main_Form
from templates.forms.filters import Filters_Form
from database.requests_db import *

from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QListWidgetItem, QGridLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QIcon, QColor, QFont
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QPushButton
from PyQt5.QtCore import QSize


class MyWidgetLogin(QMainWindow, Login_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.btn_register.clicked.connect(self.open_register)
        self.btn_entry.clicked.connect(self.check_login)

        # кнопка для быстрого входа в приложение во время разработки проекта, в конце работы над ним она убирается
        self.btn_admin = QPushButton(self)
        self.btn_admin.move(700, 520)
        self.btn_admin.clicked.connect(self.open_main)

    def initUI(self):
        self.lbl_pic = QLabel(self)
        self.pixmap = QPixmap("static/logo.png")
        self.lbl_pic.setPixmap(self.pixmap)
        self.lbl_pic.resize(250, 75)
        self.lbl_pic.move(280, 55)
        self.line_password.setEchoMode(QLineEdit.Password)

    # функция, открывающая окно регистрации по нажатию кнопки btn.register
    def open_register(self):
        self.line_password.clear()
        self.line_login.clear()
        form_login.hide()
        form_signin.show()

    # функция, обращается к функции в requests_db, проверяет наличие пользователя в системе
    def check_login(self):
        if check_user_in_system(self.line_login.text(), self.line_password.text()):
            self.open_main()
        else:
            # окно ошибки, возникающее при неверном вводе данных или отсутствия в системе
            emsg = QMessageBox(self)
            emsg.setText('Неверный логин или пароль')
            emsg.setStyleSheet('color: #FF6600')
            emsg.exec()
            self.line_password.clear()
            self.line_login.clear()

    # функция, открывающая главную страницу приложения при успешном входе в систему
    def open_main(self):
        form_login.hide()
        form_main.showMaximized()


class MyWidgetSignin(QMainWindow, Signin_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.btn_login.clicked.connect(self.open_login)
        self.btn_register.clicked.connect(self.register)
        self.line_password.setEchoMode(QLineEdit.Password)

    def initUI(self):
        self.lbl_pic = QLabel(self)
        self.pixmap = QPixmap('static/logo.png')
        self.lbl_pic.setPixmap(self.pixmap)
        self.lbl_pic.resize(250, 75)
        self.lbl_pic.move(280, 55)

    # функция, обращается к функции в requests_db, регистрирует нового пользователя в системе
    def register(self):
        res = register_new_user(self.line_login.text(), self.line_password.text())
        if res[0]:
            self.open_login()
        else:
            # окно ошибки, возникающее при неверном вводе данных или отсутствия в системе
            emsg = QMessageBox(self)
            emsg.setText(res[1])
            emsg.setStyleSheet('color: #FF6600')
            emsg.exec()
            self.line_password.clear()
            self.line_login.clear()

    # функция, открывающая страницу входа при успешной регистрации
    def open_login(self):
        form_signin.hide()
        self.line_password.clear()
        self.line_login.clear()
        form_login.show()


class MyWidgetMain(QMainWindow, Main_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.edit_find.textChanged.connect(lambda: self.edit_find.setText(self.edit_find.text().capitalize()))
        self.btn_filter.clicked.connect(lambda: form_filters.show())
        self.print_items('all')
        self.btn_all.clicked.connect(lambda: self.print_items('all'))

    def print_items(self, param):
        self.list_gadgets.clear()
        gadgets = get_gadgets(param)
        for i, el in enumerate(gadgets):
            # создание виджета
            item, widget = self.create_item(el, i)

            # добавление виджета в лист
            self.list_gadgets.addItem(item)
            self.list_gadgets.setItemWidget(item, widget)

    def create_item(self, el, i):
        item = QListWidgetItem()
        widget = QWidget()
        widget_text = QLabel(f'{str(el[0])} {el[1]}')
        widget_text.setFont(QFont('Arial', 20))
        widget_description = QPushButton('Подробнее')
        widget_description.setStyleSheet('background-color: #FF6600; color: white; height: 35px')
        widget_button = QPushButton("Добавить в корзину сравнения")
        widget_button.setStyleSheet('background-color: #FF6600; color: white; height: 50px')
        widget_price = QLabel(f'Средняя цена на Я.Маркете: {el[-1]}')
        widget_layout = QGridLayout()
        widget_layout.addWidget(widget_text)
        widget_layout.addWidget(widget_price)
        widget_layout.addWidget(widget_description)
        widget_layout.addWidget(widget_button)
        widget_layout.setSizeConstraint(QLayout.SetMaximumSize)
        widget.setLayout(widget_layout)
        item.setSizeHint(widget.sizeHint())
        item.setBackground(QColor(255, 122, 0))
        return item, widget


class MyWidgetFilters(QMainWindow, Filters_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.btn_clear.setIcon(QIcon('static/trash.png'))
        self.btn_clear.setIconSize(QSize(28, 27))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form_login = MyWidgetLogin()
    form_signin = MyWidgetSignin()
    form_main = MyWidgetMain()
    form_filters = MyWidgetFilters()
    form_login.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())