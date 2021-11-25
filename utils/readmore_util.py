from PyQt5.QtCore import QSize

from templates.forms.info import Ui_Info_Form
from PyQt5.QtWidgets import QMainWindow


class WidgetReadMore(QMainWindow, Ui_Info_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(QSize(1100, 700))