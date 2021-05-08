from analyze_screenshots.design import MainWindow
from PyQt5.QtWidgets import QApplication
from sys import argv


def main():
    app = QApplication(argv)
    main_form = MainWindow()
    main_form.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Возникла ошибка: {}".format(e))
    finally:
        print("Приложение остановлено")
