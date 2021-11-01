from templates.forms.main_wind import Main_Form

from .filters_util import MyWidgetFilters
from .readmore_util import WidgetReadMore
from database.requests_db import *

from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QWidget, QLayout, QHBoxLayout, QButtonGroup, QTableWidgetItem, \
    QMessageBox
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QFont, QColor, QPixmap


class MyWidgetMain(QMainWindow, Main_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ind_widgets = []
        self.basket_gadgets = []
        self.basket_names = []
        self.basket_data = []

        self.scroll_bar_style()

        self.form_info = WidgetReadMore()
        self.form_filters = MyWidgetFilters()

        self.btn_group_readmore = QButtonGroup()
        self.btn_group_readmore.buttonClicked.connect(self.open_read_more)
        self.btn_group_tobasket = QButtonGroup()
        self.btn_group_tobasket.buttonClicked.connect(self.add_to_basket)

        self.edit_find.textChanged.connect(lambda: self.edit_find.setText(self.edit_find.text().capitalize()))
        self.btn_filter.clicked.connect(lambda: self.form_filters.show())
        self.btn_all.clicked.connect(lambda: self.edit_find.clear())
        self.edit_find.textChanged.connect(lambda: self.print_items_in_gadgets(['search', self.edit_find.text()]))
        self.btn_clear.clicked.connect(self.clear_everything_in_table)

        self.print_items_in_gadgets(['all'])

    def scroll_bar_style(self):
        self.list_gadgets.setStyleSheet("""
                QScrollBar:vertical {              
                    background-color: #FF6600;
                    width:20px;
                }
            """)

    def print_items_in_gadgets(self, param):
        self.list_gadgets.clear()
        self.gadgets = get_gadgets(param)
        if param[-1] == '':
            self.edit_find.clear()
        self.ind_widgets.clear()
        for el in self.gadgets:
            # создание виджета
            item, widget = self.create_item_in_gadgets(el)

            # добавление виджета в лист
            self.list_gadgets.addItem(item)
            self.list_gadgets.setItemWidget(item, widget)

    def create_item_in_gadgets(self, el):
        item = QListWidgetItem()
        widget = QWidget()

        self.ind_widgets.append(el[0])

        widget_name = QLabel(el[1])
        widget_name.setFont(QFont('Arial', 20))

        widget_description = QPushButton(f'Подробнее o {el[1]}')
        widget_description.setCheckable(True)
        self.btn_group_readmore.addButton(widget_description)
        widget_description.setStyleSheet('background-color: #FF6600; color: white;'
                                         'height: 50px; border-radius: 10px; font-size: 20px')

        widget_button = QPushButton("В корзину сравнения")
        widget_button.setCheckable(True)
        self.btn_group_tobasket.addButton(widget_button)
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

    def open_read_more(self):
        self.form_info.hide()
        for el in self.gadgets:
            if self.btn_group_readmore.checkedButton().text()[12:] == el[1]:
                text = '\n\n'.join(str(el[3]).split(';'))
                self.form_info.lbl_info.setText(text)
                self.form_info.lbl_name.setText(str(el[1]))
                self.form_info.show()

    def setup_basket(self, name, data):
        self.head = ['Средняя цена', 'Производитель', 'Размер дисплея', 'Ёмкость аккумулятора',
                     'Оперативная память', 'Основная камера', 'Фронтальная камера', 'Матрица экрана']
        self.basket_names.append(name)
        self.basket_data.append(data)
        self.table_gadgets.setColumnCount(8)
        self.table_gadgets.setRowCount(5)
        self.table_gadgets.setHorizontalHeaderLabels(self.head)
        self.table_gadgets.setVerticalHeaderLabels(self.basket_names)
        self.table_gadgets.setColumnWidth(0, 215)
        self.table_gadgets.setColumnWidth(1, 215)
        self.table_gadgets.setColumnWidth(2, 200)
        self.table_gadgets.setColumnWidth(3, 215)
        self.table_gadgets.setColumnWidth(4, 215)
        self.table_gadgets.setColumnWidth(5, 190)
        self.table_gadgets.setColumnWidth(6, 190)
        self.table_gadgets.setColumnWidth(7, 190)
        self.table_gadgets.setColumnWidth(8, 190)
        self.table_gadgets.setRowCount(len(self.basket_data))
        self.print_items_in_basket()

    def add_to_basket(self):
        ind = self.ind_widgets[list(self.btn_group_tobasket.buttons()).index(self.btn_group_tobasket.checkedButton())]
        name, data = get_info_for_basket(ind)
        if name in self.basket_names:
            emsg = QMessageBox(self)
            emsg.setText('Это устройство уже в корзине сравнения')
            emsg.setStyleSheet('color: #FF6600')
            emsg.exec()
        else:
            self.setup_basket(name, data)

    def print_items_in_basket(self):
        for i, row in enumerate(self.basket_data):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                self.table_gadgets.setItem(i, j, item)

    def clear_everything_in_table(self):
        self.table_gadgets.clear()
        self.basket_names.clear()
        self.basket_data.clear()
        self.table_gadgets.setRowCount(0)
        self.table_gadgets.setColumnCount(0)


