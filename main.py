import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QSize
from templates.forms.login import Login_Form
from templates.forms.signin import Signin_Form
from templates.forms.main_wind import Main_Form
from templates.forms.filters import Filters_Form


class MyWidgetLogin(QMainWindow, Login_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.btn_register.clicked.connect(self.open_register)
        self.btn_entry.clicked.connect(self.check_login)

    def initUI(self):
        self.lbl_pic = QLabel(self)
        self.pixmap = QPixmap("static/logo.png")
        self.lbl_pic.setPixmap(self.pixmap)
        self.lbl_pic.resize(250, 75)
        self.lbl_pic.move(280, 55)

    def open_register(self):
        form_login.hide()
        form_signin.show()

    def check_login(self):
        self.open_main()

    def open_main(self):
        form_login.hide()
        form_main.showMaximized()


class MyWidgetSignin(QMainWindow, Signin_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.btn_login.clicked.connect(self.open_login)
        self.btn_register.clicked.connect(self.check_register)

    def initUI(self):
        self.lbl_pic = QLabel(self)
        self.pixmap = QPixmap('static/logo.png')
        self.lbl_pic.setPixmap(self.pixmap)
        self.lbl_pic.resize(250, 75)
        self.lbl_pic.move(280, 55)

    def check_register(self):
        pass
        self.open_login()

    def open_login(self):
        form_signin.hide()
        form_login.show()


class MyWidgetMain(QMainWindow, Main_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.edit_find.textChanged.connect(lambda: self.edit_find.setText(self.edit_find.text().capitalize()))


class MyWidgetFilters(QMainWindow, Filters_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.btn_clear.setIcon(QIcon('static/trash.png'))
        self.btn_clear.setIconSize(QSize(27, 27))


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