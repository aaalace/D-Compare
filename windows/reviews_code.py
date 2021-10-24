import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from reviews import Ui_MainWindow


class MyWidgetLogin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        screen = app.primaryScreen()
        size = screen.size()
        self.list_items.move(40, 130)
        self.list_items.resize(size.width() - 80, size.height() - 230)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidgetLogin()
    form.showMaximized()
    sys.excepthook = except_hook
    sys.exit(app.exec())
