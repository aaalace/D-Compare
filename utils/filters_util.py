from templates.forms.filters import Filters_Form

from utils.CONSTANTS.CONST_filters_util import *
from database.requests_db import *

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class MyWidgetFilters(QMainWindow, Filters_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_clear.setIcon(QIcon(LINK_TO_DEL_BTN_PIC))
        self.btn_clear.setIconSize(QSize(PIC_SIZE[0], PIC_SIZE[1]))
        self.add_filters()
        self.return_start_params()
        self.change_used_filters()

        self.btn_clear.clicked.connect(self.return_start_params)
        self.line_from.textChanged.connect(self.change_used_filters)
        self.line_to.textChanged.connect(self.change_used_filters)
        self.box_producer.currentTextChanged.connect(self.change_used_filters)
        self.box_ram.currentTextChanged.connect(self.change_used_filters)
        self.box_matrix.currentTextChanged.connect(self.change_used_filters)
        self.box_battery.currentTextChanged.connect(self.change_used_filters)
        self.box_base_camera.currentTextChanged.connect(self.change_used_filters)
        self.box_front_camera.currentTextChanged.connect(self.change_used_filters)
        self.box_display_size.currentTextChanged.connect(self.change_used_filters)

    def add_filters(self):
        self.box_producer.addItems(PRODUCER_PARAMS)
        self.box_display_size.addItems(DISPLAY_SIZE_PARAMS)
        self.box_battery.addItems(BATTERY_PARAMS)
        self.box_ram.addItems(RAM_PARAMS)
        self.box_base_camera.addItems(BASE_CAMERA_PARAMS)
        self.box_front_camera.addItems(FRONT_CAMERA_PARAMS)
        self.box_matrix.addItems(MATRIX_PARAMS)

    def return_start_params(self):
        self.line_from.setText(INITIAL_MIN_VALUE)
        self.line_to.setText(INITIAL_MAX_VALUE)
        self.box_producer.setCurrentText(INITIAL_START_PARAM)
        self.box_ram.setCurrentText(INITIAL_START_PARAM)
        self.box_matrix.setCurrentText(INITIAL_START_PARAM)
        self.box_battery.setCurrentText(INITIAL_START_PARAM)
        self.box_base_camera.setCurrentText(INITIAL_START_PARAM)
        self.box_front_camera.setCurrentText(INITIAL_START_PARAM)
        self.box_display_size.setCurrentText(INITIAL_START_PARAM)
        self.change_used_filters()

    def change_used_filters(self):
        self.text_filters.clear()
        self.text_filters.setStyleSheet('color: white; font-size: 15px')
        self.text_filters.appendPlainText(f'Цена:\n{self.line_from.text()} руб. - {self.line_to.text()} руб.\n')
        self.text_filters.appendPlainText(f'Производитель:\n{self.box_producer.currentText()}\n')
        self.text_filters.appendPlainText(f'Размер дисплея:\n{self.box_display_size.currentText()}\n')
        self.text_filters.appendPlainText(f'Ёмкость аккумулятора:\n{self.box_battery.currentText()}\n')
        self.text_filters.appendPlainText(f'Оперативная память:\n{self.box_ram.currentText()}\n')
        self.text_filters.appendPlainText(f'Основная камера:\n{self.box_base_camera.currentText()}\n')
        self.text_filters.appendPlainText(f'Фронтальная камера:\n{self.box_front_camera.currentText()}\n')
        self.text_filters.appendPlainText(f'Матрица:\n{self.box_matrix.currentText()}\n')
        self.gadgets_count()

    def gadgets_count(self):
        price = [self.line_from.text(), self.line_to.text()]
        producer = self.box_producer.currentText()
        display_size = self.box_display_size.currentText()
        battery = self.box_battery.currentText()
        ram = self.box_ram.currentText()
        base_camera = self.box_base_camera.currentText()
        front_camera = self.box_front_camera.currentText()
        matrix = self.box_matrix.currentText()
        self.gadgets = get_gadgets(['filter', [price, producer, display_size, battery, ram,
                                               base_camera, front_camera, matrix]])
        self.text_filters.appendPlainText(f'Найдено устройств: {str(len(self.gadgets))}')
