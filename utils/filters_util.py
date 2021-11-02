from templates.forms.filters import Filters_Form
from database.requests_db import *
from utils.CONSTANTS.CONST_filters_util import *

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
        self.box_producer.addItems(PRODUCER_PARAMS)
        self.box_display_size.addItems(DISPLAY_SIZE_PARAMS)
        self.box_battery.addItems(BATTERY_PARAMS)
        self.box_ram.addItems(RAM_PARAMS)
        self.box_base_camera.addItems(BASE_CAMERA_PARAMS)
        self.box_front_camera.addItems(FRONT_CAMERA_PARAMS)
        self.box_matrix.addItems(MATRIX_PARAMS)
