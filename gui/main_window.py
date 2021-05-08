# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(661, 443)
        main_window.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_img = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_img.setGeometry(QtCore.QRect(10, 10, 341, 331))
        self.groupBox_img.setObjectName("groupBox_img")
        self.pushButton_select_img = QtWidgets.QPushButton(self.groupBox_img)
        self.pushButton_select_img.setGeometry(QtCore.QRect(300, 30, 21, 21))
        self.pushButton_select_img.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../data/etc/file_manager.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_select_img.setIcon(icon)
        self.pushButton_select_img.setObjectName("pushButton_select_img")
        self.label_img = QtWidgets.QLabel(self.groupBox_img)
        self.label_img.setGeometry(QtCore.QRect(20, 60, 301, 261))
        self.label_img.setObjectName("label_img")
        self.lineEdit_path_img = QtWidgets.QLineEdit(self.groupBox_img)
        self.lineEdit_path_img.setGeometry(QtCore.QRect(10, 30, 281, 21))
        self.lineEdit_path_img.setObjectName("lineEdit_path_img")
        self.groupBox_model = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_model.setGeometry(QtCore.QRect(10, 350, 341, 61))
        self.groupBox_model.setObjectName("groupBox_model")
        self.lineEdit_path_model = QtWidgets.QLineEdit(self.groupBox_model)
        self.lineEdit_path_model.setGeometry(QtCore.QRect(10, 30, 281, 21))
        self.lineEdit_path_model.setObjectName("lineEdit_path_model")
        self.pushButton_select_model = QtWidgets.QPushButton(self.groupBox_model)
        self.pushButton_select_model.setGeometry(QtCore.QRect(300, 30, 21, 21))
        self.pushButton_select_model.setText("")
        self.pushButton_select_model.setIcon(icon)
        self.pushButton_select_model.setObjectName("pushButton_select_model")
        self.groupBox_analysis = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_analysis.setGeometry(QtCore.QRect(370, 10, 281, 291))
        self.groupBox_analysis.setObjectName("groupBox_analysis")
        self.pushButton_analyze = QtWidgets.QPushButton(self.groupBox_analysis)
        self.pushButton_analyze.setGeometry(QtCore.QRect(40, 40, 191, 25))
        self.pushButton_analyze.setObjectName("pushButton_analyze")
        self.label_info_res = QtWidgets.QLabel(self.groupBox_analysis)
        self.label_info_res.setGeometry(QtCore.QRect(60, 90, 151, 17))
        self.label_info_res.setObjectName("label_info_res")
        self.label_origin_res = QtWidgets.QLabel(self.groupBox_analysis)
        self.label_origin_res.setGeometry(QtCore.QRect(20, 120, 221, 17))
        self.label_origin_res.setObjectName("label_origin_res")
        self.label_spoof_res = QtWidgets.QLabel(self.groupBox_analysis)
        self.label_spoof_res.setGeometry(QtCore.QRect(20, 150, 221, 17))
        self.label_spoof_res.setObjectName("label_spoof_res")
        self.label_result = QtWidgets.QLabel(self.groupBox_analysis)
        self.label_result.setGeometry(QtCore.QRect(20, 200, 221, 61))
        self.label_result.setObjectName("label_result")
        self.groupBox_ceate_model = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ceate_model.setGeometry(QtCore.QRect(370, 320, 281, 91))
        self.groupBox_ceate_model.setObjectName("groupBox_ceate_model")
        self.pushButton_create_model = QtWidgets.QPushButton(self.groupBox_ceate_model)
        self.pushButton_create_model.setGeometry(QtCore.QRect(20, 40, 241, 25))
        self.pushButton_create_model.setObjectName("pushButton_create_model")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.groupBox_img.setTitle(_translate("main_window", "Выберите картинку для анализа"))
        self.label_img.setText(_translate("main_window", "TextLabel"))
        self.groupBox_model.setTitle(_translate("main_window", "Выберите файл с расширением .h5"))
        self.groupBox_analysis.setTitle(_translate("main_window", "Обработка кадра нейронной моделью"))
        self.pushButton_analyze.setText(_translate("main_window", "Анализировать фото"))
        self.label_info_res.setText(_translate("main_window", "Результат обработки"))
        self.label_origin_res.setText(_translate("main_window", "Оригинал: "))
        self.label_spoof_res.setText(_translate("main_window", "Копия: "))
        self.label_result.setText(_translate("main_window", "<html><head/><body><p>Вывод:</p><p><br/></p></body></html>"))
        self.groupBox_ceate_model.setTitle(_translate("main_window", "Работа с нейронной сетью"))
        self.pushButton_create_model.setText(_translate("main_window", "Создать модель"))
