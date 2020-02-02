import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import designw
import download
import os

class ExampleApp(QtWidgets.QMainWindow, designw.Ui_VideoDownloader):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.initUI()

    def initUI(self):
        #self.DownloadButton.clicked.connect(self.)
        self.SelWayButton.clicked.connect(self.browse_folder)


    def browse_folder(self):
            options = QFileDialog.DontUseNativeDialog
            fileName,_ = QFileDialog.getSaveFileName(self, "Выберите место сохранения файла", "",
                                                      "VideoFiles (*.mp4)", options=options)
            if fileName:
                print(fileName)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()