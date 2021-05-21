from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon

from gui import main_window, window_neural_network
from analyze_screenshots.neural_network import Model
from analyze_screenshots.utils import get_str_result


class WindowNN(QtWidgets.QDialog, window_neural_network.Ui_Dialog):
    def __init__(self, parent=None):
        super(WindowNN, self).__init__(parent)
        self.setupUi(self)
        self.path_dir = None
        self.path_dir_test = None
        folder_icon = QIcon('data/etc/file_manager.jpg')
        self.pushButton_select_dir.setIcon(folder_icon)
        self.pushButton_select_dir_test.setIcon(folder_icon)
        self.pushButton_select_dir.clicked.connect(self.browse_folder_train)
        self.pushButton_select_dir_test.clicked.connect(self.browse_folder_test)
        self.model = None
        self.pushButton_train.clicked.connect(self.train_model)
        self.name_test_res = None
        self.pushButton_test.clicked.connect(self.test_model)
        self.path_model_file = None
        self.pushButton_select_model_test.clicked.connect(self.browse_model_test)
        self.pushButton_select_model_test.setIcon(folder_icon)

    def browse_folder_train(self):
        directory_name = QtWidgets.QFileDialog.getExistingDirectory()
        self.path_dir = directory_name
        self.lineEdit_path_dir.setText(self.path_dir)

    def browse_folder_test(self):
        directory_name = QtWidgets.QFileDialog.getExistingDirectory()
        self.path_dir_test = directory_name
        self.lineEdit_path_dir_test.setText(self.path_dir_test)

    def browse_model_test(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.path_model_file = file[0]
        self.lineEdit_path_model_test.setText(self.path_model_file)

    def train_model(self):
        self.model = Model()
        epochs = int(self.lineEdit_epochs.text())
        self.model.train(epochs=epochs)
        file = self.lineEdit_name_file_model.text()
        self.model.save(file)
        self.model.get_plot(epochs)

    def test_model(self):
        model = Model()
        model.load(self.path_model_file)
        self.path_dir_test = self.lineEdit_path_dir_test.text()
        self.name_test_res = self.lineEdit_name_file_test.text()
        model.testing(self.path_dir_test, self.name_test_res)


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_img = "/run/user/1000/doc/746df25a/YOUTUBE_id24_s0_75.png"
        self.path_model = "/run/user/1000/doc/a183efa8/my_model_weights10.h5"
        self.model = None
        folder_icon = QIcon('data/etc/file_manager.jpg')
        self.pushButton_select_img.setIcon(folder_icon)
        self.pushButton_select_model.setIcon(folder_icon)
        self.pushButton_select_img.clicked.connect(self.browse_folder_img)
        self.pushButton_select_model.clicked.connect(self.browse_folder_model)
        self.pushButton_analyze.clicked.connect(self.analyze)
        self.pushButton_create_model.clicked.connect(self.run_model_window)
        self.nn_form = None

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

    def analyze(self):
        self.model = Model()
        self.model.load(self.path_model)
        result = self.model.analyse_photo(self.path_img)

        self.label_spoof_res.setText('Вероятность копии: {}'.format(result))
        self.label_origin_res.setText('Вероятность оригинала: {}'.format(1 - result))
        self.label_result.setText('Вывод: {}'.format(get_str_result(result)))

    def run_model_window(self):
        self.nn_form = WindowNN()
        self.nn_form.show()
        self.nn_form.exec_()
