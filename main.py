import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import designw
from downloadthread import DownloadingThread
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
        self.SavePath.insert(os.getcwd() + '/video.mp4')
        self.DownloadingThread_inst = DownloadingThread(mainwindow=self)
        self.ProgressBar.setValue(0)


    def browse_folder(self):
            options = QFileDialog.DontUseNativeDialog
            fileName,file = QFileDialog.getSaveFileName(self, "Выберите место сохранения файла", "video.mp4",
                                                       options=options)
            if fileName:
                self.SavePath.clear()
                if '.mp4' in fileName:
                    self.SavePath.insert(fileName)
                else:
                    self.SavePath.insert(fileName + '.mp4')


    def startdownloading(self):
        filename = self.SavePath.text().split('/')[-1]
        path = '/'.join(self.SavePath.text().split('/')[:-1])
        Error = True
        if filename in os.listdir(path):
            self.ConsoleLog.setPlainText('Файл с таким именем уже существует.')
        elif not self.SavePath.text():
            self.ConsoleLog.setPlainText('Вы не выбрали путь для сохранения файла.')
        elif not self.lineLink.text():
            self.ConsoleLog.setPlainText('Вы не ввели ссылку.')
        else:
            Error = False

        if not Error:
            self.ProgressBar.setValue(0)
            self.DownloadButton.setEnabled(False)
            self.DownloadingThread_inst.progress_sign.connect(self.updateprogressbar)
            self.ConsoleLog.setPlainText('Видео загружается...')
            self.DownloadingThread_inst.start()



    def updateprogressbar(self, val):
        self.ProgressBar.setValue(val)
        if val == 100:
            self.DownloadButton.setEnabled(True)
            self.ConsoleLog.setPlainText('Загрузка завершена.')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()