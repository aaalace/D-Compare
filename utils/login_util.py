import sys
from PyQt5.QtWidgets import QApplication

from templates.forms.login import Login_Form
from database.requests_db import *

from utils.home_util import MyWidgetMain
from utils.signin_util import MyWidgetSignin

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QPushButton


class MyWidgetLogin(QMainWindow, Login_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.sign_in = MyWidgetSignin()

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

    # функция, обращается к функции в requests_db, проверяет наличие пользователя в системе
    def check_login(self):
        if check_user_in_system(self.line_login.text(), self.line_password.text()):
            self.open_main()
        else:
            self.print_error()

    # функция, открывающая окно регистрации по нажатию кнопки btn.register
    def open_register(self):
        self.line_password.clear()
        self.line_login.clear()
        self.hide()
        self.sign_in.show()

    # функция, открывающая главную страницу приложения при успешном входе пользователя в систему
    def open_main(self):
        self.hide()
        MyWidgetMain().showMaximized()

    # окно ошибки, возникающее при неверном вводе данных или отсутствия в системе
    def print_error(self):
        emsg = QMessageBox(self)
        emsg.setText('Неверный логин или пароль')
        emsg.setStyleSheet('color: #FF6600')
        emsg.exec()
        self.line_password.clear()
        self.line_login.clear()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form_login = MyWidgetLogin()
    form_login.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
