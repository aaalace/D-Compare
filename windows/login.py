# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("background-color: #ffe3b3")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_login = QtWidgets.QLineEdit(self.centralwidget)
        self.line_login.setGeometry(QtCore.QRect(151, 171, 150, 25))
        self.line_login.setStyleSheet("background-color: #FFF")
        self.line_login.setText("")
        self.line_login.setDragEnabled(False)
        self.line_login.setPlaceholderText("")
        self.line_login.setObjectName("line_login")
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_password.setGeometry(QtCore.QRect(151, 241, 150, 25))
        self.line_password.setStyleSheet("background-color: #FFF")
        self.line_password.setObjectName("line_password")
        self.btn_entry = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entry.setGeometry(QtCore.QRect(141, 301, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_entry.setFont(font)
        self.btn_entry.setStyleSheet("background-color: white;")
        self.btn_entry.setObjectName("btn_entry")
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setGeometry(QtCore.QRect(156, 141, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_login.setFont(font)
        self.lbl_login.setStyleSheet("")
        self.lbl_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_login.setObjectName("lbl_login")
        self.lbl_password = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password.setGeometry(QtCore.QRect(156, 211, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_password.setFont(font)
        self.lbl_password.setStyleSheet("")
        self.lbl_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_password.setObjectName("lbl_password")
        self.lbl_help = QtWidgets.QLabel(self.centralwidget)
        self.lbl_help.setGeometry(QtCore.QRect(90, 370, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_help.setFont(font)
        self.lbl_help.setStyleSheet("")
        self.lbl_help.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_help.setObjectName("lbl_help")
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setGeometry(QtCore.QRect(176, 411, 90, 30))
        self.btn_register.setStyleSheet("background-color: white;")
        self.btn_register.setObjectName("btn_register")
        self.text_description = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_description.setGeometry(QtCore.QRect(420, 70, 321, 371))
        self.text_description.setStyleSheet("border-radius: 20px; background-color: white")
        self.text_description.setObjectName("text_description")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))
        self.btn_entry.setText(_translate("MainWindow", "Войти"))
        self.lbl_login.setText(_translate("MainWindow", "Логин"))
        self.lbl_password.setText(_translate("MainWindow", "Пароль"))
        self.lbl_help.setText(_translate("MainWindow", "Нет аккаунта? - Зарегистрируйся"))
        self.btn_register.setText(_translate("MainWindow", "Регистрация"))
