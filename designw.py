# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoDownloader(object):
    def setupUi(self, VideoDownloader):
        VideoDownloader.setObjectName("VideoDownloader")
        VideoDownloader.resize(590, 363)
        self.centralwidget = QtWidgets.QWidget(VideoDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.link = QtWidgets.QLabel(self.centralwidget)
        self.link.setObjectName("link")
        self.horizontalLayout_4.addWidget(self.link)
        self.lineLink = QtWidgets.QLineEdit(self.centralwidget)
        self.lineLink.setObjectName("lineLink")
        self.horizontalLayout_4.addWidget(self.lineLink)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SaveTo = QtWidgets.QLabel(self.centralwidget)
        self.SaveTo.setObjectName("SaveTo")
        self.horizontalLayout_2.addWidget(self.SaveTo)
        self.SavePath = QtWidgets.QLineEdit(self.centralwidget)
        self.SavePath.setObjectName("SavePath")
        self.horizontalLayout_2.addWidget(self.SavePath)
        self.SelWayButton = QtWidgets.QToolButton(self.centralwidget)
        self.SelWayButton.setObjectName("SelWayButton")
        self.horizontalLayout_2.addWidget(self.SelWayButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.ConsoleLog = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ConsoleLog.setReadOnly(True)
        self.ConsoleLog.setObjectName("ConsoleLog")
        self.verticalLayout.addWidget(self.ConsoleLog)
        self.verticalLayout.addWidget(self.ProgressBar)
        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setObjectName("DownloadButton")
        self.verticalLayout.addWidget(self.DownloadButton)
        VideoDownloader.setCentralWidget(self.centralwidget)
        self.retranslateUi(VideoDownloader)
        QtCore.QMetaObject.connectSlotsByName(VideoDownloader)

    def retranslateUi(self, VideoDownloader):
        _translate = QtCore.QCoreApplication.translate
        VideoDownloader.setWindowTitle(_translate("VideoDownloader", "VideoDownloader"))
        self.link.setText(_translate("VideoDownloader", "Введите ссылку:"))
        self.SaveTo.setText(_translate("VideoDownloader", "Сохранить в:"))
        self.SelWayButton.setText(_translate("VideoDownloader", "..."))
        self.DownloadButton.setText(_translate("VideoDownloader", "Скачать видео"))
