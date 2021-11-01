from templates.forms.filters import Filters_Form
from database.requests_db import *

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class MyWidgetFilters(QMainWindow, Filters_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.btn_commit.clicked.connect(lambda x: self.close())
        self.add_filters()

    def initUi(self):
        self.btn_clear.setIcon(QIcon('../static/trash.png'))
        self.btn_clear.setIconSize(QSize(28, 27))

    def add_filters(self):
        self.box_producer.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])
        self.box_display_size.addItems(['Все', '<5', '5 - 5.5', '5.6 - 6', '6.1 - 6.3', '6.4 - 6.6', '>6.6'])
        self.box_battery.addItems(['Все', '<2000 мАч', '2000-2499 мАч', '2500-2999 мАч', '3000-4499 мАч', '>4500 мАч'])
        self.box_ram.addItems(['Все', '<=2 ГБ', '3 ГБ', '4 ГБ', '6 ГБ', '8 ГБ', '>=12 ГБ'])
        self.box_base_camera.addItems(['Все', '<8 Мп', '8 Мп', '12 - 20 Мп', '21 - 40 Мп', '>40 Мп'])
        self.box_front_camera.addItems(['Все', '<2 Мп', '3 - 8 Мп', '13', '16', '>16 Мп'])
        self.box_matrix.addItems(['Все', 'IPS', 'AMOLED', 'Super AMOLED', 'OLED'])
