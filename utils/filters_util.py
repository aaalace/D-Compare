from templates.forms.filters import Filters_Form
from utils.CONSTANTS.CONST_filters_util import *

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class MyWidgetFilters(QMainWindow, Filters_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.add_filters()
        self.btn_clear.clicked.connect(self.return_start_params)

    def initUi(self):
        self.btn_clear.setIcon(QIcon('../static/trash.png'))
        self.btn_clear.setIconSize(QSize(28, 27))
        self.line_from.setText('0')
        self.line_to.setText('150000')

    def add_filters(self):
        self.box_producer.addItems(PRODUCER_PARAMS)
        self.box_display_size.addItems(DISPLAY_SIZE_PARAMS)
        self.box_battery.addItems(BATTERY_PARAMS)
        self.box_ram.addItems(RAM_PARAMS)
        self.box_base_camera.addItems(BASE_CAMERA_PARAMS)
        self.box_front_camera.addItems(FRONT_CAMERA_PARAMS)
        self.box_matrix.addItems(MATRIX_PARAMS)

    def return_start_params(self):
        self.line_from.setText('0')
        self.line_to.setText('150000')
        self.box_producer.setCurrentText('Все')
        self.box_ram.setCurrentText('Все')
        self.box_matrix.setCurrentText('Все')
        self.box_battery.setCurrentText('Все')
        self.box_base_camera.setCurrentText('Все')
        self.box_front_camera.setCurrentText('Все')
        self.box_display_size.setCurrentText('Все')