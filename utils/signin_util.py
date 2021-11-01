import os

from templates.forms.signin import Signin_Form
from database.requests_db import *


from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox


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
        self.hide()
        self.line_password.clear()
        self.line_login.clear()
        os.system('python utils/login_util.py')

