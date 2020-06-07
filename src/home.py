from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import os, re, requests, wgetter

import src.paths, src.imagebytes

if not os.path.exists(src.paths.base_path):
    os.makedirs(src.paths.base_path)
if not os.path.exists(src.paths.images_path):
    os.makedirs(src.paths.images_path)
if not os.path.exists(src.paths.export_path):
    os.makedirs(src.paths.export_path)
if not os.path.exists(src.paths.files_path):
    os.makedirs(src.paths.files_path)
if not os.path.exists(src.paths.app_list_path):
    with open(src.paths.app_list_path, 'w') as w:
        w.write('')
if not os.path.exists(src.paths.icon_path):
    with open(src.paths.icon_path, 'wb') as wb:
        wb.write(src.imagebytes.icon_bytes)

class Ui_homeMainWindow(object):
    def setup_callback(self):
        if not os.path.exists(src.paths.save_path):
            os.makedirs(src.paths.save_path)

        with open(src.paths.app_list_path, 'r') as r:
            app_list = r.readlines()
        app_list = [x.strip() for x in app_list] 

        for app in app_list:
            link = app + '/download'
            request = requests.get(link)
            source = request.content
            soup = BeautifulSoup(source, 'lxml')
            app_name = soup.find('h1', class_='name').text
            download_link_soup = soup.find('a', class_="data download")
            download_link = download_link_soup.get('href')
            filename = wgetter.download(download_link, outdir=src.paths.save_path)
            os.rename(filename,r'EzSetup Downloads\\'+app_name+'.exe')

    def setupUi(self, homeMainWindow):
        homeMainWindow.setObjectName("homeMainWindow")
        homeMainWindow.setFixedSize(750, 200)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        homeMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homeMainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(homeMainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.softwarePushButton = QtWidgets.QPushButton(self.centralWidget)
        self.softwarePushButton.setGeometry(QtCore.QRect(0, 0, 250, 125))
        self.softwarePushButton.setObjectName("softwarePushButton")
        self.filesPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.filesPushButton.setGeometry(QtCore.QRect(250, 0, 250, 125))
        self.filesPushButton.setObjectName("filesPushButton")
        self.backgroundPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.backgroundPushButton.setGeometry(QtCore.QRect(500, 0, 250, 125))
        self.backgroundPushButton.setObjectName("backgroundPushButton")
        self.softwareCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.softwareCheckBox.setGeometry(QtCore.QRect(120, 80, 13, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.softwareCheckBox.setFont(font)
        self.softwareCheckBox.setText("")
        self.softwareCheckBox.setObjectName("softwareCheckBox")
        self.filesCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.filesCheckBox.setGeometry(QtCore.QRect(370, 80, 13, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.filesCheckBox.setFont(font)
        self.filesCheckBox.setText("")
        self.filesCheckBox.setObjectName("filesCheckBox")
        self.backgroundCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.backgroundCheckBox.setGeometry(QtCore.QRect(620, 80, 13, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.backgroundCheckBox.setFont(font)
        self.backgroundCheckBox.setText("")
        self.backgroundCheckBox.setObjectName("backgroundCheckBox")
        self.importPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.importPushButton.setGeometry(QtCore.QRect(0, 125, 125, 75))
        self.importPushButton.setObjectName("importPushButton")
        self.exportPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.exportPushButton.setGeometry(QtCore.QRect(625, 125, 125, 75))
        self.exportPushButton.setObjectName("exportPushButton")
        self.setupPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.setupPushButton.setGeometry(QtCore.QRect(125, 125, 500, 75))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.setupPushButton.setFont(font)
        self.setupPushButton.setObjectName("setupPushButton")
        homeMainWindow.setCentralWidget(self.centralWidget)

        self.softwarePushButton.clicked.connect(homeMainWindow.software)
        self.filesPushButton.clicked.connect(homeMainWindow.files)
        self.backgroundPushButton.clicked.connect(homeMainWindow.background)
        self.importPushButton.clicked.connect(homeMainWindow.import_button)
        self.exportPushButton.clicked.connect(homeMainWindow.export_button)
        self.setupPushButton.clicked.connect(self.setup_callback)

        self.retranslateUi(homeMainWindow)
        QtCore.QMetaObject.connectSlotsByName(homeMainWindow)

    def retranslateUi(self, homeMainWindow):
        _translate = QtCore.QCoreApplication.translate
        homeMainWindow.setWindowTitle(_translate("homeMainWindow", "EZSetup"))
        self.softwarePushButton.setText(_translate("homeMainWindow", "Software"))
        self.filesPushButton.setText(_translate("homeMainWindow", "Files"))
        self.backgroundPushButton.setText(_translate("homeMainWindow", "Background"))
        self.importPushButton.setText(_translate("homeMainWindow", "Import"))
        self.exportPushButton.setText(_translate("homeMainWindow", "Export"))
        self.setupPushButton.setText(_translate("homeMainWindow", "Setup"))