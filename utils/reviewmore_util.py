from templates.forms.review import Ui_Info_Form
from PyQt5.QtWidgets import QMainWindow


class WidgetReviewMore(QMainWindow, Ui_Info_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)