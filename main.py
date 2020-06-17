from PyQt5.QtWidgets import QMainWindow, QApplication
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
        src.qtObjects.file_browse()
        webbrowser.open(src.paths.tempImportPath)
    def export_button(self):
        zipObject = zipfile.ZipFile(src.paths.current_dir + '\\' + src.paths.current_time + '.ez', 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(src.paths.tempExportPath) + 1
        for base, dirs, files in os.walk(src.paths.tempExportPath):
            for file in files:
                fn = os.path.join(base, file)
                zipObject.write(fn, fn[rootlen:])

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