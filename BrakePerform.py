# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrakePerform.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(821, 751)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 821, 751))
        self.label.setStyleSheet("image: url(:/newPrefix/wheelNum.jpg);\n"
"background-color: rgb(0, 170, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(200, 100, 71, 31))
        self.label_1.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(550, 100, 71, 31))
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 210, 71, 31))
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(550, 210, 71, 31))
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 320, 71, 31))
        self.label_5.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(550, 320, 71, 31))
        self.label_6.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(200, 430, 71, 31))
        self.label_7.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(550, 430, 71, 31))
        self.label_8.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(200, 540, 71, 31))
        self.label_9.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(550, 530, 71, 31))
        self.label_10.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Brake Performance", "Brake Performance"))
import wheelNum_rc
