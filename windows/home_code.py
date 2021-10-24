import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from home import QMainWindow


class MyWidgetLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.

    def initUI(self):
        uic.loadUi('../design files/home.ui', self)
        screen = app.primaryScreen()
        size = screen.size()
        print(size.width(), size.height())
        self.list_items.move(30, int(size.height() / 5))
        self.list_items.resize(int(size.width()) - 60, (int(size.height() / 1.4)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidgetLogin()
    form.showMaximized()
    sys.excepthook = except_hook
    sys.exit(app.exec())
