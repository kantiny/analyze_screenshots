from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.uic import loadUi

from gui import main_window, window_neural_network
from analyze_screenshots.neural_network import Model
from analyze_screenshots.utils import get_str_result


class WindowNN:
    def __init__(self):
        self.ui = loadUi('gui/window_neural_network.ui')


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_img = None
        self.path_model = None
        folder_img = QIcon('data/etc/file_manager.jpg')
        self.pushButton_select_img.setIcon(folder_img)
        self.pushButton_select_model.setIcon(folder_img)
        self.pushButton_select_img.clicked.connect(self.browse_folder_img)
        folder_img = QIcon('data/etc/file_manager.jpg')
        self.pushButton_select_img.setIcon(folder_img)
        self.pushButton_select_model.clicked.connect(self.browse_folder_model)
        self.pushButton_analyze.clicked.connect(self.analyze)

    def browse_folder_img(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName()
        self.path_img = file_name[0]
        self.lineEdit_path_img.setText(self.path_img)
        test_img = QPixmap(self.path_img)
        self.label_img.setPixmap(test_img)

    def browse_folder_model(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName()
        self.path_model = file_name[0]
        self.lineEdit_path_model.setText(self.path_model)

    def analyze(self, model: Model):
        model.load(self.path_model)
        result = model.analyse_photo(self.path_img)
        self.label_spoof_res.setText('Вероятность копии: {}'.format(result))
        self.label_origin_res.setText('Вероятность оригинала: {}'.format(1 - result))
        self.label_result.setText('Вывод: {}'.format(get_str_result(result)))

    def run_model_window(self):
        nn_form = WindowNN()
        nn_form.ui.show()
