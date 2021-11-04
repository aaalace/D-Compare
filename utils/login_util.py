import sys
from PyQt5.QtWidgets import QApplication

from templates.forms.login import Login_Form
from database.requests_db import *
from utils.CONSTANTS.CONST_login_util import *

from utils.home_util import MyWidgetMain
from utils.signin_util import MyWidgetSignin

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QPushButton


class MyWidgetLogin(QMainWindow, Login_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lbl_pic = QLabel(self)
        self.pixmap = QPixmap(LINK_TO_LOGO)
        self.lbl_pic.setPixmap(self.pixmap)
        self.lbl_pic.resize(LOGO_IMAGE_SIZE[0], LOGO_IMAGE_SIZE[1])
        self.lbl_pic.move(LOGO_IMAGE_MOVE[0], LOGO_IMAGE_MOVE[1])
        self.line_password.setEchoMode(QLineEdit.Password)
        self.sign_in = MyWidgetSignin()

        self.btn_register.clicked.connect(self.open_register)
        self.btn_entry.clicked.connect(self.check_login)

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
        error = QMessageBox(self)
        error.setText(ERROR_TEXT)
        error.setStyleSheet(ERROR_STYLE)
        error.exec()
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
