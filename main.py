from PyQt5.QtWidgets import QMainWindow, QApplication
from zipfile import ZipFile
import os, shutil, sys

from src.home import Ui_homeMainWindow
from src.software import Ui_softwareMainWindow
from src.files import Ui_filesMainWindow
from src.background import Ui_backgroundMainWindow
import src.paths, src.imagebytes

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
        #import action
        x = x
    def export_button(self):
        from os.path import basename
        with ZipFile(src.paths.current_time+'.ez', 'w') as zipObj:
            for folderName, subfolders, filenames in os.walk(src.paths.export_path):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath, basename(filePath))

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
    shutil.rmtree(src.paths.export_path, ignore_errors=True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app_exit)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())