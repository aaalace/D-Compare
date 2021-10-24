# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basket.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1886, 1055)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: #ffe3b3")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_items = QtWidgets.QListWidget(self.centralwidget)
        self.list_items.setGeometry(QtCore.QRect(55, 80, 1781, 901))
        self.list_items.setStyleSheet("background-color: white")
        self.list_items.setObjectName("list_items")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(870, 10, 140, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: orange; color: white; ")
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1886, 26))
        self.menubar.setObjectName("menubar")
        self.menu_home = QtWidgets.QMenu(self.menubar)
        self.menu_home.setObjectName("menu_home")
        self.menu_basket = QtWidgets.QMenu(self.menubar)
        self.menu_basket.setObjectName("menu_basket")
        self.menu_review = QtWidgets.QMenu(self.menubar)
        self.menu_review.setGeometry(QtCore.QRect(231, 153, 159, 54))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menu_review.setFont(font)
        self.menu_review.setStyleSheet("")
        self.menu_review.setSeparatorsCollapsible(False)
        self.menu_review.setObjectName("menu_review")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menubar.addAction(self.menu_home.menuAction())
        self.menubar.addAction(self.menu_basket.menuAction())
        self.menubar.addAction(self.menu_review.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная страница"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить все"))
        self.menu_home.setTitle(_translate("MainWindow", "Главная"))
        self.menu_basket.setTitle(_translate("MainWindow", "Корзина сравнения"))
        self.menu_review.setTitle(_translate("MainWindow", "Обзоры и рекомендации"))
        self.action.setText(_translate("MainWindow", "сц"))
