# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reviews.ui'
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
        MainWindow.setStyleSheet("background-color: #353232")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_find = QtWidgets.QLabel(self.centralwidget)
        self.lbl_find.setGeometry(QtCore.QRect(480, 20, 1011, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lbl_find.setFont(font)
        self.lbl_find.setStyleSheet("color: #FF6600")
        self.lbl_find.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_find.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_find.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_find.setScaledContents(False)
        self.lbl_find.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_find.setObjectName("lbl_find")
        self.list_items = QtWidgets.QListWidget(self.centralwidget)
        self.list_items.setGeometry(QtCore.QRect(50, 130, 1786, 851))
        self.list_items.setStyleSheet("background-color: white")
        self.list_items.setObjectName("list_items")
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
        self.lbl_find.setText(_translate("MainWindow", "Обзоры и рекомендации"))
        self.menu_home.setTitle(_translate("MainWindow", "Главная"))
        self.menu_basket.setTitle(_translate("MainWindow", "Корзина сравнения"))
        self.menu_review.setTitle(_translate("MainWindow", "Обзоры и рекомендации"))
        self.action.setText(_translate("MainWindow", "сц"))
