from PyQt5.QtWidgets import QMainWindow, QApplication
from bs4 import BeautifulSoup
import os, re, requests, shutil, sys, webbrowser, wgetter, zipfile

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
        if not os.path.exists(src.paths.import_path):
            os.makedirs(src.paths.import_path)
        src.qtObjects.file_browse()
        webbrowser.open(src.paths.import_path)
    def export_button(self):
        zipObject = zipfile.ZipFile(src.paths.current_dir + '\\' + src.paths.current_time + '.ez', 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(src.paths.export_path) + 1
        for base, dirs, files in os.walk(src.paths.export_path):
            for file in files:
                fn = os.path.join(base, file)
                zipObject.write(fn, fn[rootlen:])
    def setup_button(self):
        if not os.path.exists(src.paths.save_path):
            os.makedirs(src.paths.save_path)

        with open(src.paths.import_app_list_path, 'r') as r:
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
    shutil.rmtree(src.paths.temp_path, ignore_errors=True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app_exit)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())