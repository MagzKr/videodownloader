import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread
import time
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
        self.DownloadButton.clicked.connect(self.startdownloading)
        self.SelWayButton.clicked.connect(self.browse_folder)
        self.SaveWay.insert(os.getcwd() + '/video.mp4')
        self.DownloadingThread_inst = DownloadingThread(mainwindow=self)


    def browse_folder(self):
            options = QFileDialog.DontUseNativeDialog
            fileName,file = QFileDialog.getSaveFileName(self, "Выберите место сохранения файла", "video.mp4",
                                                       options=options)
            if fileName:
                self.SaveWay.clear()
                if '.mp4' in fileName:
                    self.SaveWay.insert(fileName)
                else:
                    self.SaveWay.insert(fileName + '.mp4')


    def startdownloading(self):
        self.DownloadingThread_inst.start()


class DownloadingThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow


    def run(self):
        self.mainwindow.ConsoleLog.insertPlainText('Вы не выбрали путь для сохранения файла или не ввели ссылку.')
        if self.mainwindow.SaveWay.text() and self.mainwindow.lineLink.text():
             download.start_download(self.mainwindow.SaveWay.text(), self.mainwindow.ConsoleLog,
                                     self.mainwindow.lineLink.text())
        # else:
        #     self.mainwindow.ConsoleLog.setPlainText('Вы не выбрали путь для сохранения файла или не ввели ссылку.')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()