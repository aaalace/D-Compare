import os

from templates.forms.signin import Signin_Form
from database.requests_db import *
from utils.CONSTANTS.CONST_signin_util import *


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
        self.pixmap = QPixmap(LINK_TO_LOGO)
        self.lbl_pic.setPixmap(self.pixmap)
        self.lbl_pic.resize(LOGO_IMAGE_SIZE[0], LOGO_IMAGE_SIZE[1])
        self.lbl_pic.move(LOGO_IMAGE_MOVE[0], LOGO_IMAGE_MOVE[1])

    # функция, обращается к функции в requests_db, регистрирует нового пользователя в системе
    def register(self):
        res = register_new_user(self.line_login.text(), self.line_password.text())
        if res[0]:
            self.open_login()
        else:
            # окно ошибки, возникающее при неверном вводе данных или отсутствия в системе
            error = QMessageBox(self)
            error.setText(res[1])
            error.setStyleSheet(ERROR_STYLE)
            error.exec()
            self.line_password.clear()
            self.line_login.clear()

    # функция, открывающая страницу входа при успешной регистрации
    def open_login(self):
        self.hide()
        self.line_password.clear()
        self.line_login.clear()
        os.system(OS_FILE)

