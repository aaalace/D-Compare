from templates.forms.main_wind import Main_Form
from templates.forms.filters import Filters_Form
from database.requests_db import *

from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QWidget, QLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QFont, QColor, QIcon, QPixmap
from PyQt5.QtCore import QSize


class MyWidgetMain(QMainWindow, Main_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scroll_bar_style()
        form_filters = MyWidgetFilters()

        self.edit_find.textChanged.connect(lambda: self.edit_find.setText(self.edit_find.text().capitalize()))
        self.btn_filter.clicked.connect(lambda: form_filters.show())
        self.print_items(['all'])
        self.btn_all.clicked.connect(lambda: self.print_items(['all']))
        self.edit_find.textChanged.connect(lambda: self.print_items(['search', self.edit_find.text()]))

    def print_items(self, param):
        self.list_gadgets.clear()
        if param[0] == 'all':
            self.edit_find.clear()
        gadgets = get_gadgets(param)
        for i, el in enumerate(gadgets):
            # создание виджета
            item, widget = self.create_item(el, i)

            # добавление виджета в лист
            self.list_gadgets.addItem(item)
            self.list_gadgets.setItemWidget(item, widget)

    def create_item(self, el, i):
        item = QListWidgetItem()
        widget = QWidget()
        widget_name = QLabel(el[1])
        widget_name.setFont(QFont('Arial', 20))
        widget_description = QPushButton('Подробнее')
        widget_description.setStyleSheet('background-color: #FF6600; color: white;'
                                         'height: 50px; border-radius: 10px; font-size: 20px')
        widget_button = QPushButton("Добавить в корзину сравнения")
        widget_button.setStyleSheet('background-color: #FF6600; color: white; height: 50px;'
                                    ' border-radius: 10px; font-size: 20px')
        widget_price = QLabel(f'Средняя цена на Яндекс.Маркете: {el[-1]}')
        widget_price.setFont(QFont('Arial', 12))
        widget_pic = QLabel(self)
        if not bool(el[2]):
            pixmap = QPixmap('static/spare.png')
        else:
            pixmap = QPixmap(el[2])
        pixmap2 = pixmap.scaledToWidth(227)
        pixmap3 = pixmap2.scaledToHeight(227)
        widget_pic.setPixmap(pixmap3)
        widget_layout = QHBoxLayout()
        widget_layout.addWidget(widget_pic)
        widget_layout.addWidget(widget_name)
        widget_layout.addWidget(widget_price)
        widget_layout.addWidget(widget_description)
        widget_layout.addWidget(widget_button)
        widget_layout.setSizeConstraint(QLayout.SetMaximumSize)
        widget.setLayout(widget_layout)
        item.setSizeHint(widget.sizeHint())
        item.setBackground(QColor(255, 122, 0))
        return item, widget

    def scroll_bar_style(self):
        self.list_gadgets.setStyleSheet("""
                QScrollBar:vertical {              
                    background-color: #FF6600;
                    width:20px;
                }
            """)


class MyWidgetFilters(QMainWindow, Filters_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.btn_commit.clicked.connect(lambda x: self.close())
        self.add_filters()

    def initUi(self):
        self.btn_clear.setIcon(QIcon('static/trash.png'))
        self.btn_clear.setIconSize(QSize(28, 27))

    def add_filters(self):
        self.box_producer.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])
        self.box_display_size.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])
        self.box_ghz.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])
        self.box_ram.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])
        self.box_matrix.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])
        self.box_base_camera.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])
        self.box_front_camera.addItems(['Все', 'Apple', 'Samsung', 'Xiaomi', 'Poco', 'OnePlus', 'Huawei'])