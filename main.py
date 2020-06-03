from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from home import Ui_homeMainWindow
from software import Ui_softwareMainWindow
from files import Ui_filesMainWindow
from background import Ui_backgroundMainWindow

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
        #export action
        x = x
    def setup(self):
        #setup action
        x = x

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())