import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from templates.forms.filters import Ui_MainWindow


class MyWidgetLogin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.btn_clear.setIcon(QIcon('../static/trash.png'))
        self.btn_clear.setIconSize(QSize(27, 27))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidgetLogin()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
