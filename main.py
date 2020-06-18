from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil, sys, webbrowser, zipfile

from src.home import Ui_homeMainWindow
from src.software import Ui_softwareMainWindow
from src.files import Ui_filesMainWindow
from src.background import Ui_backgroundMainWindow
import src.paths, src.imagebytes, src.qtObjects

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_homeMainWindow()
        self.ui.setupUi(self)
    def software(self):
        self.softwareWindow = softwareWindow()
        self.softwareWindow.show()
    def files(self):
        self.filesWindow = filesWindow()
        self.filesWindow.show()
    def background(self):
        self.backgroundWindow = backgroundWindow()
        self.backgroundWindow.show()
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
            webbrowser.open(src.paths.tempImportPath)
        except:
            src.qtObjects.error_message("EXPx01")

class softwareWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_softwareMainWindow()
        self.ui.setupUi(self)
class filesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_filesMainWindow()
        self.ui.setupUi(self)
class backgroundWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_backgroundMainWindow()
        self.ui.setupUi(self)

def app_exit():
    shutil.rmtree(src.paths.tempBasePath, ignore_errors=True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app_exit)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())