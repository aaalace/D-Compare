# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fillers.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Filters_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 752)
        MainWindow.setStyleSheet("background-color: #353232")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 351, 711))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 10, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_1.setFont(font)
        self.lbl_1.setStyleSheet("color: #FF6600")
        self.lbl_1.setObjectName("lbl_1")
        self.verticalLayout.addWidget(self.lbl_1)
        self.box_f1 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_f1.sizePolicy().hasHeightForWidth())
        self.box_f1.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.box_f1.setPalette(palette)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.box_f1.setFont(font)
        self.box_f1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.box_f1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.box_f1.setStyleSheet("background-color: white")
        self.box_f1.setObjectName("box_f1")
        self.verticalLayout.addWidget(self.box_f1)
        self.lbl_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_2.setFont(font)
        self.lbl_2.setStyleSheet("color: #FF6600")
        self.lbl_2.setObjectName("lbl_2")
        self.verticalLayout.addWidget(self.lbl_2)
        self.box_f2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.box_f2.setPalette(palette)
        self.box_f2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.box_f2.setStyleSheet("background-color: white")
        self.box_f2.setObjectName("box_f2")
        self.verticalLayout.addWidget(self.box_f2)
        self.lbl_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_3.setFont(font)
        self.lbl_3.setStyleSheet("color: #FF6600")
        self.lbl_3.setObjectName("lbl_3")
        self.verticalLayout.addWidget(self.lbl_3)
        self.box_f3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.box_f3.setPalette(palette)
        self.box_f3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.box_f3.setStyleSheet("background-color: white")
        self.box_f3.setObjectName("box_f3")
        self.verticalLayout.addWidget(self.box_f3)
        self.lbl_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_4.setFont(font)
        self.lbl_4.setStyleSheet("color: #FF6600")
        self.lbl_4.setObjectName("lbl_4")
        self.verticalLayout.addWidget(self.lbl_4)
        self.box_f4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.box_f4.setPalette(palette)
        self.box_f4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.box_f4.setStyleSheet("background-color: white")
        self.box_f4.setObjectName("box_f4")
        self.verticalLayout.addWidget(self.box_f4)
        self.lbl_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_5.setFont(font)
        self.lbl_5.setStyleSheet("color: #FF6600")
        self.lbl_5.setObjectName("lbl_5")
        self.verticalLayout.addWidget(self.lbl_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_from = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_from.setStyleSheet("color: #FF6600")
        self.lbl_from.setObjectName("lbl_from")
        self.horizontalLayout.addWidget(self.lbl_from)
        self.line_from = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_from.setStyleSheet("background-color: white")
        self.line_from.setObjectName("line_from")
        self.horizontalLayout.addWidget(self.line_from)
        self.lbl_to = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_to.setStyleSheet("color: #FF6600")
        self.lbl_to.setObjectName("lbl_to")
        self.horizontalLayout.addWidget(self.lbl_to)
        self.line_to = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_to.setStyleSheet("background-color: white")
        self.line_to.setObjectName("line_to")
        self.horizontalLayout.addWidget(self.line_to)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbl_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_6.setFont(font)
        self.lbl_6.setStyleSheet("color: #FF6600")
        self.lbl_6.setObjectName("lbl_6")
        self.verticalLayout.addWidget(self.lbl_6)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.horizontalScrollBar.setPalette(palette)
        self.horizontalScrollBar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.horizontalScrollBar.setStyleSheet("background-color: white")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        self.text_filters = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_filters.setEnabled(False)
        self.text_filters.setGeometry(QtCore.QRect(390, 110, 341, 511))
        self.text_filters.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text_filters.setStyleSheet("background-color: white")
        self.text_filters.setObjectName("text_filters")
        self.label_filtres = QtWidgets.QLabel(self.centralwidget)
        self.label_filtres.setGeometry(QtCore.QRect(390, 30, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_filtres.setFont(font)
        self.label_filtres.setStyleSheet("color: #FF6600")
        self.label_filtres.setAlignment(QtCore.Qt.AlignCenter)
        self.label_filtres.setObjectName("label_filtres")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(530, 660, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_clear.setPalette(palette)
        self.btn_clear.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.btn_clear.setAutoFillBackground(False)
        self.btn_clear.setStyleSheet("background-color: white")
        self.btn_clear.setText("")
        self.btn_clear.setObjectName("btn_clear")
        self.lbl_del = QtWidgets.QLabel(self.centralwidget)
        self.lbl_del.setGeometry(QtCore.QRect(410, 660, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_del.setFont(font)
        self.lbl_del.setStyleSheet("color: #FF6600")
        self.lbl_del.setObjectName("lbl_del")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 640, 151, 91))
        self.label.setStyleSheet("color: white")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фильтр"))
        self.lbl_1.setText(_translate("MainWindow", "фильтр 1"))
        self.lbl_2.setText(_translate("MainWindow", "фильтр 2"))
        self.lbl_3.setText(_translate("MainWindow", "фильтр 3"))
        self.lbl_4.setText(_translate("MainWindow", "фильтр 4"))
        self.lbl_5.setText(_translate("MainWindow", "фильтр 5"))
        self.lbl_from.setText(_translate("MainWindow", "от"))
        self.lbl_to.setText(_translate("MainWindow", "до"))
        self.lbl_6.setText(_translate("MainWindow", "фильтр 6"))
        self.label_filtres.setText(_translate("MainWindow", "Примененные фильтры"))
        self.lbl_del.setText(_translate("MainWindow", "Очистить все"))
        self.label.setText(_translate("MainWindow", "Устройств соответствующих параметрам: 100"))
