from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from ctypes import wintypes
import ctypes, os, requests, shutil, struct, webbrowser, wgetter, zipfile

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
    if not os.path.exists(src.paths.tempExportPath+'\\Background'):
        os.makedirs(src.paths.tempExportPath+'\\Background')
    if not os.path.exists(src.paths.exportFilesPath):
        os.makedirs(src.paths.exportFilesPath)
    if not os.path.exists(src.paths.exportFontsPath):
        os.makedirs(src.paths.exportFontsPath)
except:
    src.qtObjects.error_message("SYSx01")
try:
    if not os.path.exists(src.paths.permIconPath):
        with open(src.paths.permIconPath, 'wb') as wb:
            wb.write(src.imagebytes.icon_bytes)
    if not os.path.exists(src.paths.exportBackgroundSourcePath):
        with open(src.paths.exportBackgroundSourcePath, 'w') as w:
            w.write('')
    if not os.path.exists(src.paths.exportFilesListPath):
        with open(src.paths.exportFilesListPath, 'w') as w:
            w.write('')
    if not os.path.exists(src.paths.exportFontsListPath):
        with open(src.paths.exportFontsListPath, 'w') as w:
            w.write('')
    if not os.path.exists(src.paths.exportSoftwareListPath):
        with open(src.paths.exportSoftwareListPath, 'w') as w:
            w.write('')
    if not os.path.exists(src.paths.exportSoftwareLinksPath):
        with open(src.paths.exportSoftwareLinksPath, 'w') as w:
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
        self.export_folderAction = QtWidgets.QAction(homeMainWindow)
        self.export_folderAction.setObjectName("export_folderAction")
        self.import_folderAction = QtWidgets.QAction(homeMainWindow)
        self.import_folderAction.setObjectName("import_folderAction")
        self.fileMenu.addAction(self.importAction)
        self.fileMenu.addAction(self.exportAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.import_folderAction)
        self.fileMenu.addAction(self.export_folderAction)
        self.helpMenu.addAction(self.github_repositryAction)
        self.MenuBar.addAction(self.fileMenu.menuAction())
        self.MenuBar.addAction(self.helpMenu.menuAction())


        self.softwarePushButton.clicked.connect(homeMainWindow.software)
        self.filesPushButton.clicked.connect(homeMainWindow.files)
        self.fontsPushButton.clicked.connect(homeMainWindow.fonts)
        self.backgroundPushButton.clicked.connect(homeMainWindow.background)
        self.setupPushButton.clicked.connect(self.setup_button)
        self.importAction.triggered.connect(self.import_button)
        self.exportAction.triggered.connect(self.export_button)
        self.import_folderAction.triggered.connect(self.import_folder)
        self.export_folderAction.triggered.connect(self.export_folder)


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
        self.export_folderAction.setText(_translate("homeMainWindow", "Export Folder"))
        self.import_folderAction.setText(_translate("homeMainWindow", "Import Folder"))


    def setup_button(self):
        ########## Background ##########
        if struct.calcsize('P') * 8 == 64:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, src.paths.importBackgroundPath, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoA(20, 0, src.paths.importBackgroundPath, 3)
        
        ########## Files ##########
        shutil.copytree(src.paths.importFilesPath, src.paths.files_save_path)

        ########## Fonts ##########
        from ctypes import wintypes
        try:
            import winreg
        except ImportError:
            import _winreg as winreg
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)
        FONTS_REG_PATH = r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'
        HWND_BROADCAST   = 0xFFFF
        SMTO_ABORTIFHUNG = 0x0002
        WM_FONTCHANGE    = 0x001D
        GFRI_DESCRIPTION = 1
        GFRI_ISTRUETYPE  = 3
        if not hasattr(wintypes, 'LPDWORD'):
            wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)
        user32.SendMessageTimeoutW.restype = wintypes.LPVOID
        user32.SendMessageTimeoutW.argtypes = (wintypes.HWND, wintypes.UINT, wintypes.LPVOID, wintypes.LPVOID, wintypes.UINT, wintypes.UINT, wintypes.LPVOID)
        gdi32.AddFontResourceW.argtypes = (wintypes.LPCWSTR,)
        gdi32.GetFontResourceInfoW.argtypes = (wintypes.LPCWSTR, wintypes.LPDWORD, wintypes.LPVOID, wintypes.DWORD)
        for file_ in os.listdir(src.paths.importFontsPath):
            if file_.endswith('.ttf') or file_.endswith('.otf'):
                src_path = os.path.join(src.paths.importFontsPath, file_)
                dst_path = os.path.join(os.environ['SystemRoot'], 'Fonts', os.path.basename(src_path))
                shutil.copy(src_path, dst_path)
                if not gdi32.AddFontResourceW(dst_path):
                    os.remove(dst_path)
                    raise WindowsError('AddFontResource failed to load "%s"' % src_path)
                user32.SendMessageTimeoutW(HWND_BROADCAST, WM_FONTCHANGE, 0, 0, SMTO_ABORTIFHUNG, 1000, None)
                filename = os.path.basename(dst_path)
                fontname = os.path.splitext(filename)[0]
                cb = wintypes.DWORD()
                if gdi32.GetFontResourceInfoW(filename, ctypes.byref(cb), None, GFRI_DESCRIPTION):
                    buf = (ctypes.c_wchar * cb.value)()
                    if gdi32.GetFontResourceInfoW(filename, ctypes.byref(cb), buf, GFRI_DESCRIPTION):
                        fontname = buf.value
                is_truetype = wintypes.BOOL()
                cb.value = ctypes.sizeof(is_truetype)
                gdi32.GetFontResourceInfoW(filename, ctypes.byref(cb), ctypes.byref(is_truetype), GFRI_ISTRUETYPE)
                if is_truetype:
                    fontname += ' (TrueType)'
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, FONTS_REG_PATH, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, fontname, 0, winreg.REG_SZ, filename)

        ########## Software ##########
        if not os.path.exists(src.paths.software_save_path):
            os.makedirs(src.paths.software_save_path)
        with open(src.paths.importSoftwareLinksPath, 'r') as r:
            software_list = r.readlines()
        software_list = [x.strip() for x in software_list] 
        for software in software_list:
            link = software + 'post_download'
            request = requests.get(link)
            source = request.text
            soup = BeautifulSoup(source, 'html.parser')
            download_link = soup.find('script', type='text/javascript', attrs={'data-qa-download-url':True})
            download_link = download_link.get('data-qa-download-url')
            filename = wgetter.download(download_link, outdir=src.paths.software_save_path)


    def import_button(self):
        if not os.path.exists(src.paths.tempImportPath):
            os.makedirs(src.paths.tempImportPath)
        try:
            QFileDialog = QtWidgets.QFileDialog()
            QFilter = "EzSetup File (*.ez)"
            current_dir = os.getcwd()
            file_name = QtWidgets.QFileDialog.getOpenFileName(parent=QFileDialog, caption="Select File", directory=current_dir, filter=QFilter)
        except:
            src.qtObjects.error_message("IMPx01")
        if file_name[0] != '':
            try:
                with zipfile.ZipFile(file_name[0], 'r') as zipObject:
                    zipObject.extractall(src.paths.tempImportPath)
                src.qtObjects.success_message()
                webbrowser.open(src.paths.tempImportPath)
            except:
                src.qtObjects.error_message("IMPx02")


    def export_button(self):
        zipObject = zipfile.ZipFile(src.paths.current_dir + '\\' + src.paths.current_time + '.ez', 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(src.paths.tempExportPath) + 1
        try:
            for base, dirs, files in os.walk(src.paths.tempExportPath):
                for file in files:
                    fn = os.path.join(base, file)
                    zipObject.write(fn, fn[rootlen:])
            src.qtObjects.success_message()
            webbrowser.open(src.paths.current_dir)
        except:
            src.qtObjects.error_message("EXPx01")
    def import_folder(self):
        webbrowser.open(src.paths.tempImportPath)
    def export_folder(self):
        webbrowser.open(src.paths.tempExportPath)