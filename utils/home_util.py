from templates.forms.main_wind import Main_Form

from .filters_util import MyWidgetFilters
from .readmore_util import WidgetReadMore
from database.requests_db import *
from utils.CONSTANTS.CONST_home_util import *

from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QWidget, QLayout, \
    QHBoxLayout, QButtonGroup, QTableWidgetItem, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QFont, QColor, QPixmap


class MyWidgetMain(QMainWindow, Main_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ind_widgets = WIDGET_INDEX
        self.basket_gadgets = GADGETS_IN_BASKET
        self.basket_names = NAMES_IN_BASKET
        self.basket_data = DATA_IN_BASKET

        self.form_info = WidgetReadMore()
        self.form_filters = MyWidgetFilters()

        self.btn_group_readmore = QButtonGroup()
        self.btn_group_readmore.buttonClicked.connect(self.open_read_more)
        self.btn_group_tobasket = QButtonGroup()
        self.btn_group_tobasket.buttonClicked.connect(self.add_to_basket)

        self.edit_find.textChanged.connect(lambda: self.edit_find.setText(self.edit_find.text().capitalize()))
        self.edit_find.textChanged.connect(lambda: self.get_gadgets_by_search(['search', self.edit_find.text()]))
        self.btn_filter.clicked.connect(lambda: self.show_filters())
        self.btn_all.clicked.connect(lambda: self.get_gadgets_by_search(['all', '']))
        self.btn_all.clicked.connect(lambda: self.edit_find.clear())
        self.btn_all.clicked.connect(lambda: self.form_filters.return_start_params())
        self.btn_clear.clicked.connect(self.clear_everything_in_basket)
        self.form_filters.btn_commit.clicked.connect(self.get_gadgets_by_params)
        self.radio_update.clicked.connect(self.change_pass_echo)
        self.btn_update.clicked.connect(self.change_password)

        self.scroll_bar_style()
        self.table_gadgets.setStyleSheet(TABLE_BASKET_WITH_ITEMS_STYLE)
        self.get_gadgets_by_search(['all'])
        self.get_username_password()

    def scroll_bar_style(self):
        self.list_gadgets.setStyleSheet(SCROLL_STYLE)

    def show_filters(self):
        self.form_filters.hide()
        self.form_filters.show()

    def get_gadgets_by_params(self):
        self.form_filters.close()
        self.list_gadgets.clear()
        price = [self.form_filters.line_from.text(), self.form_filters.line_to.text()]
        producer = self.form_filters.box_producer.currentText()
        display_size = self.form_filters.box_display_size.currentText()
        battery = self.form_filters.box_battery.currentText()
        ram = self.form_filters.box_ram.currentText()
        base_camera = self.form_filters.box_base_camera.currentText()
        front_camera = self.form_filters.box_front_camera.currentText()
        matrix = self.form_filters.box_matrix.currentText()
        self.gadgets = get_gadgets(['filter', [price, producer, display_size, battery, ram,
                               base_camera, front_camera, matrix]])
        self.print_items_in_list_gadgets()

    def get_gadgets_by_search(self, param):
        self.list_gadgets.clear()
        self.gadgets = get_gadgets(param)
        self.print_items_in_list_gadgets()

    def print_items_in_list_gadgets(self):
        self.ind_widgets.clear()
        for el in self.gadgets:
            # создание виджета
            item, widget = self.create_item_in_list_gadgets(el)

            # добавление виджета в лист
            self.list_gadgets.addItem(item)
            self.list_gadgets.setItemWidget(item, widget)

    def create_item_in_list_gadgets(self, el):
        item = QListWidgetItem()
        widget = QWidget()

        self.ind_widgets.append(el[0])

        widget_name = QLabel(el[1])
        widget_name.setFont(QFont(WIDGET_NAME_FONT[0], WIDGET_NAME_FONT[1]))

        btn_description = QPushButton(f'Подробнее o {el[1]}')
        btn_description.setCheckable(True)
        self.btn_group_readmore.addButton(btn_description)
        btn_description.setStyleSheet(BTN_DESC_STYLE)

        btn_add = QPushButton(BTN_ADD_TEXT)
        btn_add.setCheckable(True)
        self.btn_group_tobasket.addButton(btn_add)
        btn_add.setStyleSheet(BTN_ADD_STYLE)

        widget_price = QLabel(f'Средняя цена на Яндекс.Маркете: {el[-1]}')
        widget_price.setFont(QFont(WIDGET_PRICE_FONT[0], WIDGET_PRICE_FONT[1]))

        widget_pic = QLabel(self)
        if not bool(el[2]):
            pixmap = QPixmap(SPARE_PIC_LINK)
        else:
            pixmap = QPixmap(el[2])
        pixmap2 = pixmap.scaledToWidth(IMAGE_SIZE)
        pixmap3 = pixmap2.scaledToHeight(IMAGE_SIZE)
        widget_pic.setPixmap(pixmap3)

        widget_layout = QHBoxLayout()
        widget_layout.addWidget(widget_pic)
        widget_layout.addWidget(widget_name)
        widget_layout.addWidget(widget_price)
        widget_layout.addWidget(btn_description)
        widget_layout.addWidget(btn_add)
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

    def add_to_basket(self):
        ind = self.ind_widgets[list(self.btn_group_tobasket.buttons()).index(self.btn_group_tobasket.checkedButton())]
        name, data = get_info_for_basket(ind)
        if name in self.basket_names:
            error = QMessageBox(self)
            error.setText(ERROR_TEXT)
            error.setStyleSheet(ERROR_STYLE)
            error.exec()
        else:
            self.btn_group_tobasket.checkedButton().setStyleSheet(BTN_ADD_CHECKED_STYLE)
            self.btn_group_tobasket.checkedButton().setText(BTN_ADD_CHECKED_TEXT)
            self.setup_basket(name, data)

    def setup_basket(self, name, data):
        self.head = TABLE_BASKET_HEADER
        self.basket_names.append(name)
        self.basket_data.append(data)
        self.table_gadgets.setColumnCount(8)
        self.table_gadgets.setRowCount(5)
        self.table_gadgets.setHorizontalHeaderLabels(self.head)
        self.table_gadgets.setVerticalHeaderLabels(self.basket_names)
        self.table_gadgets.setColumnWidth(0, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(1, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(2, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(3, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(4, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(5, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(6, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(7, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setColumnWidth(8, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setRowCount(len(self.basket_data))
        self.table_gadgets.setStyleSheet(TABLE_BASKET_WITHOUT_ITEMS_STYLE)
        self.print_items_in_basket()

    def print_items_in_basket(self):
        for i, row in enumerate(self.basket_data):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                self.table_gadgets.setItem(i, j, item)

    def clear_everything_in_basket(self):
        self.table_gadgets.setStyleSheet(TABLE_BASKET_WITH_ITEMS_STYLE)
        self.table_gadgets.clear()
        self.basket_names.clear()
        self.basket_data.clear()
        self.table_gadgets.setRowCount(0)
        self.table_gadgets.setColumnCount(0)
        for el in self.btn_group_tobasket.buttons():
            el.setStyleSheet(BTN_ADD_STYLE)
            el.setText(BTN_ADD_TEXT)

    def get_username_password(self):
        user, pas = check_user_in_system(0, 0)
        self.line_login.setText(user)
        self.line_password.setText(pas)
        self.line_password.setEchoMode(QLineEdit.Password)

    def change_pass_echo(self):
        if self.radio_update.isChecked():
            self.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.line_password.setEchoMode(QLineEdit.Password)

    def change_password(self):
        self.line_password.setText(update_password(self.line_new.text(), self.line_login.text()))