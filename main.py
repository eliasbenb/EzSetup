from PyQt5.QtWidgets import QMainWindow, QApplication
import os, shutil, sys

from src.home import Ui_homeMainWindow
from src.background import Ui_backgroundMainWindow
from src.files import Ui_filesMainWindow
from src.fonts import Ui_fontsMainWindow
from src.software import Ui_softwareMainWindow
import src.paths, src.imagebytes, src.qtObjects

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_homeMainWindow()
        self.ui.setupUi(self)
    def background(self):
        self.backgroundWindow = backgroundWindow()
        self.backgroundWindow.show()
    def files(self):
        self.filesWindow = filesWindow()
        self.filesWindow.show()
    def fonts(self):
        self.fontsWindow = fontsWindow()
        self.fontsWindow.show()
    def software(self):
        self.softwareWindow = softwareWindow()
        self.softwareWindow.show()

class backgroundWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_backgroundMainWindow()
        self.ui.setupUi(self)
class filesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_filesMainWindow()
        self.ui.setupUi(self)
class fontsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_fontsMainWindow()
        self.ui.setupUi(self)
class softwareWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_softwareMainWindow()
        self.ui.setupUi(self)

def app_exit():
    shutil.rmtree(src.paths.tempBasePath, ignore_errors=True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app_exit)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())