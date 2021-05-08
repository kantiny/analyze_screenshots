# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_neural_network.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 318)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 61))
        self.groupBox.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_path_img = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_path_img.setGeometry(QtCore.QRect(10, 30, 351, 21))
        self.lineEdit_path_img.setObjectName("lineEdit_path_img")
        self.pushButton_select_img = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_select_img.setGeometry(QtCore.QRect(380, 30, 21, 21))
        self.pushButton_select_img.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../data/etc/file_manager.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_select_img.setIcon(icon)
        self.pushButton_select_img.setObjectName("pushButton_select_img")
        self.groupBox_model = QtWidgets.QGroupBox(Dialog)
        self.groupBox_model.setGeometry(QtCore.QRect(10, 80, 411, 61))
        self.groupBox_model.setObjectName("groupBox_model")
        self.lineEdit_name_file = QtWidgets.QLineEdit(self.groupBox_model)
        self.lineEdit_name_file.setGeometry(QtCore.QRect(10, 30, 391, 21))
        self.lineEdit_name_file.setObjectName("lineEdit_name_file")
        self.groupBox_epochs = QtWidgets.QGroupBox(Dialog)
        self.groupBox_epochs.setGeometry(QtCore.QRect(10, 150, 201, 61))
        self.groupBox_epochs.setObjectName("groupBox_epochs")
        self.lineEdit_epochs = QtWidgets.QLineEdit(self.groupBox_epochs)
        self.lineEdit_epochs.setGeometry(QtCore.QRect(50, 30, 101, 21))
        self.lineEdit_epochs.setObjectName("lineEdit_epochs")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(228, 180, 181, 25))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_test = QtWidgets.QGroupBox(Dialog)
        self.groupBox_test.setGeometry(QtCore.QRect(10, 220, 411, 91))
        self.groupBox_test.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.groupBox_test.setObjectName("groupBox_test")
        self.lineEdit_path_img_test = QtWidgets.QLineEdit(self.groupBox_test)
        self.lineEdit_path_img_test.setGeometry(QtCore.QRect(10, 30, 351, 21))
        self.lineEdit_path_img_test.setObjectName("lineEdit_path_img_test")
        self.pushButton_select_img_test = QtWidgets.QPushButton(self.groupBox_test)
        self.pushButton_select_img_test.setGeometry(QtCore.QRect(380, 30, 21, 21))
        self.pushButton_select_img_test.setText("")
        self.pushButton_select_img_test.setIcon(icon)
        self.pushButton_select_img_test.setObjectName("pushButton_select_img_test")
        self.pushButton_test = QtWidgets.QPushButton(self.groupBox_test)
        self.pushButton_test.setGeometry(QtCore.QRect(110, 60, 181, 25))
        self.pushButton_test.setObjectName("pushButton_test")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Выберите дирректорию с обучающей выборкой"))
        self.groupBox_model.setTitle(_translate("Dialog", "Введите имя файла, в котором будет сохранена модель"))
        self.groupBox_epochs.setTitle(_translate("Dialog", "Выберите количество эпох"))
        self.pushButton.setText(_translate("Dialog", "Обучить модель"))
        self.groupBox_test.setTitle(_translate("Dialog", "Выберите дирректорию c тестовыми данными"))
        self.pushButton_test.setText(_translate("Dialog", "Обучить модель"))
