# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info_Form(object):
    def setupUi(self, Info_Form):
        Info_Form.setObjectName("Info_Form")
        Info_Form.resize(892, 609)
        Info_Form.setStyleSheet("background-color: #353232")
        self.lbl_name = QtWidgets.QLabel(Info_Form)
        self.lbl_name.setGeometry(QtCore.QRect(30, 20, 831, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("color: #FF6600")
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_info = QtWidgets.QLabel(Info_Form)
        self.lbl_info.setGeometry(QtCore.QRect(30, 90, 831, 491))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_info.setFont(font)
        self.lbl_info.setStyleSheet("color: white")
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setObjectName("lbl_info")

        self.retranslateUi(Info_Form)
        QtCore.QMetaObject.connectSlotsByName(Info_Form)

    def retranslateUi(self, Info_Form):
        _translate = QtCore.QCoreApplication.translate
        Info_Form.setWindowTitle(_translate("Info_Form", "Характеристики"))
        self.lbl_name.setText(_translate("Info_Form", "TextLabel"))
        self.lbl_info.setText(_translate("Info_Form", "TextLabel"))
