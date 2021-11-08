import sys
from PyQt5.QtWidgets import QApplication
from utils.login_util import MyWidgetLogin


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form_login = MyWidgetLogin()
    form_login.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
