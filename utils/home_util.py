from PIL.ImageQt import ImageQt
from PIL import Image


from templates.forms.main_wind import Main_Form

from .filters_util import MyWidgetFilters
from .readmore_util import WidgetReadMore
from .reviewmore_util import WidgetReviewMore
from utils.requests_db import *
from utils.CONSTANTS.CONST_home_util import *

from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QWidget, QLayout, \
    QHBoxLayout, QButtonGroup, QTableWidgetItem, QMessageBox, QLineEdit, QInputDialog
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QFont, QColor, QPixmap


class MyWidgetMain(QMainWindow, Main_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ind_gadgets = []
        self.ind_reviews = []
        self.basket_gadgets = []
        self.basket_names = []
        self.basket_data = []

        self.form_info = WidgetReadMore()
        self.form_filters = MyWidgetFilters()
        self.form_review = WidgetReviewMore()

        self.btn_group_readmore = QButtonGroup()
        self.btn_group_readmore.buttonClicked.connect(self.open_read_more)
        self.btn_group_tobasket = QButtonGroup()
        self.btn_group_tobasket.buttonClicked.connect(self.add_to_basket)
        self.btn_group_reviews = QButtonGroup()
        self.btn_group_reviews.buttonClicked.connect(self.open_more_about_review)

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
        self.table_gadgets.setStyleSheet(TABLE_BASKET_WITHOUT_ITEMS_STYLE)
        self.get_gadgets_by_search(['all'])
        self.get_username_password()
        self.get_reviews()

    # вспомогательные функции:

    # добавление стиля для ползунка в list_gadgets
    def scroll_bar_style(self):
        self.list_gadgets.setStyleSheet(SCROLL_STYLE_VERT)

    # функция для открытия окна фильтров
    def show_filters(self):
        self.form_filters.hide()
        self.form_filters.show()

    # функции отвечающие за главную страницу:

    # функция для получения гаджетов по параметрам фильтра
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

    # функция для получения гаджетов по параметрам поисковой строки
    def get_gadgets_by_search(self, param):
        self.list_gadgets.clear()
        self.gadgets = get_gadgets(param)
        self.print_items_in_list_gadgets()

    # функция для вывода на экран гаджетов в list_gadgets
    def print_items_in_list_gadgets(self):
        self.ind_gadgets.clear()
        for el in self.gadgets:
            # создание виджета
            item, widget = self.create_item_in_list_gadgets(el)

            # добавление виджета в лист
            self.list_gadgets.addItem(item)
            self.list_gadgets.setItemWidget(item, widget)

    # функция создания виджета для каждого гаджета в list_gadgets
    def create_item_in_list_gadgets(self, el):
        item = QListWidgetItem()
        widget = QWidget()

        self.ind_gadgets.append(el[0])

        widget_name = QLabel(el[1])
        widget_name.setFont(QFont(WIDGET_NAME_FONT[0], WIDGET_NAME_FONT[1]))

        btn_description = QPushButton(f'Подробнее')
        btn_description.setCheckable(True)
        self.btn_group_readmore.addButton(btn_description)
        btn_description.setStyleSheet(BTN_DESC_STYLE)

        btn_add = QPushButton(BTN_ADD_TEXT)
        btn_add.setCheckable(True)
        self.btn_group_tobasket.addButton(btn_add)
        btn_add.setStyleSheet(BTN_ADD_STYLE)

        widget_pic = QLabel(self)
        if not bool(el[2]):
            img = Image.open(SPARE_PIC_LINK)
            img.resize((150, 150))
            qim = ImageQt(img)
            pixmap = QPixmap.fromImage(qim)
        else:
            img = Image.open(el[2])
            img.resize((150, 150))
            qim = ImageQt(img)
            pixmap = QPixmap.fromImage(qim)
        pixmap = pixmap.scaledToWidth(IMAGE_SIZE)
        pixmap = pixmap.scaledToHeight(IMAGE_SIZE)
        widget_pic.setPixmap(pixmap)

        widget_layout = QHBoxLayout()
        widget_layout.addWidget(widget_pic)
        widget_layout.addWidget(widget_name)
        widget_layout.addWidget(btn_description)
        widget_layout.addWidget(btn_add)
        widget_layout.setSizeConstraint(QLayout.SetMaximumSize)
        widget.setLayout(widget_layout)
        item.setSizeHint(widget_layout.sizeHint())
        item.setBackground(QColor(ORANGE[0], ORANGE[1], ORANGE[2]))
        return item, widget

    # функция для открытия окна по нажатию кнопки "Подробнее"
    def open_read_more(self):
        self.form_info.hide()
        ind = self.ind_gadgets[list(self.btn_group_readmore.buttons()).index(self.btn_group_readmore.checkedButton())]
        name, data = get_readmore_by_button(ind)
        data = data[0][0].split(';')
        data = self.convert_characteristics(data)
        text = '\n\n'.join(data)
        self.form_info.lbl_info.setText(text)
        self.form_info.lbl_name.setText(name)
        self.form_info.show()

    def convert_characteristics(self, data):
        for i, el in enumerate(data):
            if i == 0:
                data[i] = f'Средняя цена устройства на Яндекс.Маркете - {el}'
            if i == 1:
                data[i] = f'Производитель - {el}'
            if i == 2:
                data[i] = f'Размер экрана - {el}"'
            if i == 3:
                data[i] = f'Ёмкость аккумулятора - {el} мАч'
            if i == 4:
                data[i] = f'Оперативная память: - {el} ГБ'
            if i == 5:
                data[i] = f'Основная камера - {el} Мп'
            if i == 6:
                data[i] = f'Фронтальная камера: - {el} Мп'
            if i == 7:
                data[i] = f'Тип матрицы - {el}'
        return data

    # функции отвечающие за корзину сравнения:

    # функция для добавления гаджета и характеристики в корзину сравнения
    def add_to_basket(self):
        ind = self.ind_gadgets[list(self.btn_group_tobasket.buttons()).index(self.btn_group_tobasket.checkedButton())]
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

    # функция для создания таблицы в корзине сравнения
    def setup_basket(self, name, data):
        self.head = TABLE_BASKET_HEADER
        self.basket_names.append(name)
        self.basket_data.append(data)
        self.table_gadgets.setRowCount(8)
        self.table_gadgets.setColumnCount(len(self.basket_data))
        self.table_gadgets.setHorizontalHeaderLabels(self.basket_names)
        self.table_gadgets.setVerticalHeaderLabels(self.head)
        if len(self.basket_names) <= 5:
            height = TABLE_BASKET_ROW_HEIGHT_LESS_6
        else:
            height = TABLE_BASKET_ROW_HEIGHT_MORE_6
        for i in range(9):
            self.table_gadgets.setRowHeight(i, height)
        for i in range(len(self.basket_names)):
            self.table_gadgets.setColumnWidth(i, TABLE_BASKET_COLUMN_WIDTH)
        self.table_gadgets.setStyleSheet(TABLE_BASKET_WITH_ITEMS_STYLE)
        self.print_items_in_basket()

    # функция для вывода на экран гаджетов и их характеристик в table_gadgets в корзине сравнения
    def print_items_in_basket(self):
        for i, row in enumerate(self.basket_data):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                color = QColor(255, 255, 255)
                item.setBackground(color)
                color1 = QColor(0, 0, 0)
                item.setForeground(color1)
                self.table_gadgets.setItem(j, i, item)

    # функция для очистки корзины сравнения
    def clear_everything_in_basket(self):
        self.table_gadgets.setStyleSheet(TABLE_BASKET_WITHOUT_ITEMS_STYLE)
        self.table_gadgets.clear()
        self.basket_names.clear()
        self.basket_data.clear()
        self.table_gadgets.setRowCount(0)
        self.table_gadgets.setColumnCount(0)
        for el in self.btn_group_tobasket.buttons():
            el.setStyleSheet(BTN_ADD_STYLE)
            el.setText(BTN_ADD_TEXT)

    # функции отвечающие за страницу профиль:

    # функция для получения логина и пароля пользователя
    def get_username_password(self):
        user, pas = check_user_in_system(0, 0)
        self.line_login.setText(user)
        self.line_password.setText(pas)
        self.line_password.setEchoMode(QLineEdit.Password)

    # функция для переключения echo mode пароля на странице профиля
    def change_pass_echo(self):
        if self.radio_update.isChecked():
            self.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.line_password.setEchoMode(QLineEdit.Password)

    # функция для изменения пароля
    def change_password(self):
        dialog = QInputDialog()
        dialog.setStyleSheet(DIALOG_STYLE)
        text, ok = dialog.getText(dialog, DIALOG_TITLE,
                                          DIALOG_TEXT)

        if ok:
            updated_password = update_password(text, self.line_login.text())
            self.line_password.setText(updated_password)

    # функции отвечающие за страницу обзоры и рекомендации:

    # функция для получения списка статей
    def get_reviews(self):
        self.reviews = get_reviews()
        self.print_items_in_list_reviews()

    # функция для вывода на экран всех обзоров в list_reviews
    def print_items_in_list_reviews(self):
        for el in self.reviews:
            # создание виджета
            item, widget = self.create_item_in_list_reviews(el)

            # добавление виджета в лист
            self.list_reviews.setStyleSheet(REVIEW_STYLE)
            self.list_reviews.addItem(item)
            self.list_reviews.setItemWidget(item, widget)

    # функция для создания виджета каждого обзора
    def create_item_in_list_reviews(self, el):
        item = QListWidgetItem()
        widget = QWidget()

        self.ind_reviews.append(el[0])

        btn_more = QPushButton(el[1])
        btn_more.setCheckable(True)

        self.btn_group_reviews.addButton(btn_more)
        btn_more.setStyleSheet(BTN_READ_MORE)

        widget_layout = QHBoxLayout()
        widget_layout.addWidget(btn_more)
        widget_layout.setSizeConstraint(QLayout.SetMaximumSize)
        widget_layout.addStretch()
        widget_layout.setSpacing(20)
        widget.setLayout(widget_layout)
        widget.setStyleSheet(REVIEW_STYLE)
        item.setSizeHint(widget.sizeHint())
        item.setBackground(QColor(ORANGE[0], ORANGE[1], ORANGE[2]))
        return item, widget

    def open_more_about_review(self):
        self.form_review.hide()
        index = self.ind_reviews[list(self.btn_group_reviews.buttons()).index(self.btn_group_reviews.checkedButton())]
        review, info = get_reviews_by_button(index)
        self.form_review.text_data.setPlainText(info[0])
        self.form_review.lbl_name.setText(review)
        self.form_review.show()