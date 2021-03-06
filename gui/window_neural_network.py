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
        Dialog.resize(430, 470)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 61))
        self.groupBox.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_path_dir = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_path_dir.setGeometry(QtCore.QRect(10, 30, 351, 21))
        self.lineEdit_path_dir.setObjectName("lineEdit_path_dir")
        self.pushButton_select_dir = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_select_dir.setGeometry(QtCore.QRect(380, 30, 21, 21))
        self.pushButton_select_dir.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../data/etc/file_manager.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_select_dir.setIcon(icon)
        self.pushButton_select_dir.setObjectName("pushButton_select_dir")
        self.groupBox_model = QtWidgets.QGroupBox(Dialog)
        self.groupBox_model.setGeometry(QtCore.QRect(10, 80, 411, 61))
        self.groupBox_model.setObjectName("groupBox_model")
        self.lineEdit_name_file_model = QtWidgets.QLineEdit(self.groupBox_model)
        self.lineEdit_name_file_model.setGeometry(QtCore.QRect(10, 30, 391, 21))
        self.lineEdit_name_file_model.setObjectName("lineEdit_name_file_model")
        self.groupBox_epochs = QtWidgets.QGroupBox(Dialog)
        self.groupBox_epochs.setGeometry(QtCore.QRect(10, 150, 201, 61))
        self.groupBox_epochs.setObjectName("groupBox_epochs")
        self.lineEdit_epochs = QtWidgets.QLineEdit(self.groupBox_epochs)
        self.lineEdit_epochs.setGeometry(QtCore.QRect(50, 30, 101, 21))
        self.lineEdit_epochs.setObjectName("lineEdit_epochs")
        self.pushButton_train = QtWidgets.QPushButton(Dialog)
        self.pushButton_train.setGeometry(QtCore.QRect(228, 180, 181, 25))
        self.pushButton_train.setObjectName("pushButton_train")
        self.groupBox_test = QtWidgets.QGroupBox(Dialog)
        self.groupBox_test.setGeometry(QtCore.QRect(10, 290, 411, 61))
        self.groupBox_test.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.groupBox_test.setObjectName("groupBox_test")
        self.lineEdit_path_dir_test = QtWidgets.QLineEdit(self.groupBox_test)
        self.lineEdit_path_dir_test.setGeometry(QtCore.QRect(10, 30, 351, 21))
        self.lineEdit_path_dir_test.setObjectName("lineEdit_path_dir_test")
        self.pushButton_select_dir_test = QtWidgets.QPushButton(self.groupBox_test)
        self.pushButton_select_dir_test.setGeometry(QtCore.QRect(380, 30, 21, 21))
        self.pushButton_select_dir_test.setText("")
        self.pushButton_select_dir_test.setIcon(icon)
        self.pushButton_select_dir_test.setObjectName("pushButton_select_dir_test")
        self.pushButton_test = QtWidgets.QPushButton(Dialog)
        self.pushButton_test.setGeometry(QtCore.QRect(80, 430, 271, 25))
        self.pushButton_test.setObjectName("pushButton_test")
        self.groupBox_test_file = QtWidgets.QGroupBox(Dialog)
        self.groupBox_test_file.setGeometry(QtCore.QRect(10, 360, 411, 61))
        self.groupBox_test_file.setObjectName("groupBox_test_file")
        self.lineEdit_name_file_test = QtWidgets.QLineEdit(self.groupBox_test_file)
        self.lineEdit_name_file_test.setGeometry(QtCore.QRect(10, 30, 391, 21))
        self.lineEdit_name_file_test.setObjectName("lineEdit_name_file_test")
        self.groupBox_test_model = QtWidgets.QGroupBox(Dialog)
        self.groupBox_test_model.setGeometry(QtCore.QRect(10, 220, 411, 61))
        self.groupBox_test_model.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.groupBox_test_model.setObjectName("groupBox_test_model")
        self.lineEdit_path_model_test = QtWidgets.QLineEdit(self.groupBox_test_model)
        self.lineEdit_path_model_test.setGeometry(QtCore.QRect(10, 30, 351, 21))
        self.lineEdit_path_model_test.setObjectName("lineEdit_path_model_test")
        self.pushButton_select_model_test = QtWidgets.QPushButton(self.groupBox_test_model)
        self.pushButton_select_model_test.setGeometry(QtCore.QRect(380, 30, 21, 21))
        self.pushButton_select_model_test.setText("")
        self.pushButton_select_model_test.setIcon(icon)
        self.pushButton_select_model_test.setObjectName("pushButton_select_model_test")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "???????????????? ?????????????????????? ?? ?????????????????? ????????????????"))
        self.groupBox_model.setTitle(_translate("Dialog", "?????????????? ?????? ??????????, ?? ?????????????? ?????????? ?????????????????? ????????????"))
        self.groupBox_epochs.setTitle(_translate("Dialog", "???????????????? ???????????????????? ????????"))
        self.pushButton_train.setText(_translate("Dialog", "?????????????? ????????????"))
        self.groupBox_test.setTitle(_translate("Dialog", "???????????????? ?????????????????????? c ?????????????????? ??????????????"))
        self.pushButton_test.setText(_translate("Dialog", "?????????????????????? ???????????????????? ????????????"))
        self.groupBox_test_file.setTitle(_translate("Dialog", "?????????????? ?????? ??????????, ?? ?????????????? ???????????????? ??????????????????"))
        self.groupBox_test_model.setTitle(_translate("Dialog", "???????????????? ???????? c ?????????????? ?????? ????????????????????????"))
