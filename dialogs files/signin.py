import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class MyWidgetSignin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('../design files/signin.ui', self)
        self.lbl_pic = QLabel(self)
        self.pixmap = QPixmap('../static/logo.png')
        self.lbl_pic.setPixmap(self.pixmap)
        self.lbl_pic.resize(230, 70)
        self.lbl_pic.move(110, 50)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidgetSignin()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
