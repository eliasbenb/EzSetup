from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import ctypes, os, re, requests, shutil, struct, webbrowser, wgetter

import src.paths, src.imagebytes, src.qtObjects

try:
    if not os.path.exists(src.paths.permBasePath):
        os.makedirs(src.paths.permBasePath)
    if not os.path.exists(src.paths.permImagesPath):
        os.makedirs(src.paths.permImagesPath)
    if not os.path.exists(src.paths.tempBasePath):
        os.makedirs(src.paths.tempBasePath)
    if not os.path.exists(src.paths.tempExportPath):
        os.makedirs(src.paths.tempExportPath)
    if not os.path.exists(src.paths.tempImportPath):
        os.makedirs(src.paths.tempImportPath)
    if not os.path.exists(src.paths.exportInfoPath):
        os.makedirs(src.paths.exportInfoPath)
    if not os.path.exists(src.paths.importInfoPath):
        os.makedirs(src.paths.importInfoPath)
    if not os.path.exists(src.paths.exportFilesPath):
        os.makedirs(src.paths.exportFilesPath)
    if not os.path.exists(src.paths.exportFontsPath):
        os.makedirs(src.paths.exportFontsPath)
    if not os.path.exists(src.paths.tempExportPath+'\\Background'):
        os.makedirs(src.paths.tempExportPath+'\\Background')
    if not os.path.exists(src.paths.tempExportPath+'\\Software'):
        os.makedirs(src.paths.tempExportPath+'\\Software')
except:
    src.qtObjects.error_message("SYSx01")
try:
    if not os.path.exists(src.paths.exportSoftwarePath):
        with open(src.paths.exportSoftwarePath, 'w') as w:
            w.write('')
    if not os.path.exists(src.paths.permIconPath):
        with open(src.paths.permIconPath, 'wb') as wb:
            wb.write(src.imagebytes.icon_bytes)
    if not os.path.exists(src.paths.exportFilesListPath):
        with open(src.paths.exportFilesListPath, 'w') as w:
            w.write('')
except:
    src.qtObjects.error_message("SYSx02")

class Ui_homeMainWindow(object):
    def setupUi(self, homeMainWindow):
        homeMainWindow.setObjectName("homeMainWindow")
        homeMainWindow.setFixedSize(800, 230)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        homeMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.permIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homeMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(homeMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backgroundPushButton.setGeometry(QtCore.QRect(-1, 0, 201, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.backgroundPushButton.setFont(font)
        self.backgroundPushButton.setObjectName("backgroundPushButton")
        self.filesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.filesPushButton.setGeometry(QtCore.QRect(200, 0, 200, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.filesPushButton.setFont(font)
        self.filesPushButton.setObjectName("filesPushButton")
        self.fontsPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.fontsPushButton.setGeometry(QtCore.QRect(400, 0, 200, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.fontsPushButton.setFont(font)
        self.fontsPushButton.setObjectName("fontsPushButton")
        self.softwarePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.softwarePushButton.setGeometry(QtCore.QRect(600, 0, 201, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.softwarePushButton.setFont(font)
        self.softwarePushButton.setObjectName("softwarePushButton")
        self.setupPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.setupPushButton.setGeometry(QtCore.QRect(0, 130, 801, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.setupPushButton.setFont(font)
        self.setupPushButton.setObjectName("setupPushButton")
        homeMainWindow.setCentralWidget(self.centralwidget)
        self.MenuBar = QtWidgets.QMenuBar(homeMainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.MenuBar.setObjectName("MenuBar")
        self.fileMenu = QtWidgets.QMenu(self.MenuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.helpMenu = QtWidgets.QMenu(self.MenuBar)
        self.helpMenu.setObjectName("helpMenu")
        homeMainWindow.setMenuBar(self.MenuBar)
        self.importAction = QtWidgets.QAction(homeMainWindow)
        self.importAction.setObjectName("importAction")
        self.exportAction = QtWidgets.QAction(homeMainWindow)
        self.exportAction.setObjectName("exportAction")
        self.github_repositryAction = QtWidgets.QAction(homeMainWindow)
        self.github_repositryAction.setObjectName("github_repositryAction")
        self.fileMenu.addAction(self.importAction)
        self.fileMenu.addAction(self.exportAction)
        self.helpMenu.addAction(self.github_repositryAction)
        self.MenuBar.addAction(self.fileMenu.menuAction())
        self.MenuBar.addAction(self.helpMenu.menuAction())

        self.softwarePushButton.clicked.connect(homeMainWindow.software)
        self.filesPushButton.clicked.connect(homeMainWindow.files)
        self.backgroundPushButton.clicked.connect(homeMainWindow.background)
        self.setupPushButton.clicked.connect(self.setup_button)
        self.importAction.triggered.connect(homeMainWindow.import_button)
        self.exportAction.triggered.connect(homeMainWindow.export_button)

        self.retranslateUi(homeMainWindow)
        QtCore.QMetaObject.connectSlotsByName(homeMainWindow)

    def retranslateUi(self, homeMainWindow):
        _translate = QtCore.QCoreApplication.translate
        homeMainWindow.setWindowTitle(_translate("homeMainWindow", "EzSetup"))
        self.backgroundPushButton.setText(_translate("homeMainWindow", "Background"))
        self.filesPushButton.setText(_translate("homeMainWindow", "Files"))
        self.fontsPushButton.setText(_translate("homeMainWindow", "Fonts"))
        self.softwarePushButton.setText(_translate("homeMainWindow", "Software"))
        self.setupPushButton.setText(_translate("homeMainWindow", "Setup"))
        self.fileMenu.setTitle(_translate("homeMainWindow", "File"))
        self.helpMenu.setTitle(_translate("homeMainWindow", "Help"))
        self.importAction.setText(_translate("homeMainWindow", "Import"))
        self.exportAction.setText(_translate("homeMainWindow", "Export"))
        self.github_repositryAction.setText(_translate("homeMainWindow", "GitHub Repositry"))

    def setup_button(self):
        def software_setup(self):
            if not os.path.exists(src.paths.software_save_path):
                os.makedirs(src.paths.software_save_path)
            with open(src.paths.importSoftwarePath, 'r') as r:
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
                filename = wgetter.download(download_link, outdir=src.paths.software_save_path)
                os.rename(filename,src.paths.software_save_path+app_name+'.exe')
        def files_setup(self):
            shutil.copytree(src.paths.importFilesPath, src.paths.files_save_path)
        def background_setup(self):
            if struct.calcsize('P') * 8 == 64:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, src.paths.importBackgroundPath, 3)
            else:
                ctypes.windll.user32.SystemParametersInfoA(20, 0, src.paths.importBackgroundPath, 3)
