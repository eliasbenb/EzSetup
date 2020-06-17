from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import os, re, requests

import src.paths, src.imagebytes, src.qtObjects

class Ui_softwareMainWindow(object):
    def callback(self):
        try:
            query = self.queryLineEdit.text()
            link = "https://en.uptodown.com/windows/search/"+query
            request = requests.get(link)
            source = request.content
            soup = BeautifulSoup(source, 'lxml')
            app_link = soup.find('a', attrs={'title': re.compile("^download")})
            app_link = app_link.get('href')
            with open(src.paths.exportSoftwarePath, 'a+') as w:
                w.write(str(app_link))
                w.write('\n')
            item = QtGui.QStandardItem(app_link)
            self.model.appendRow(item)
            src.qtObjects.success_message()
        except:
            src.qtObjects.error_message()

    def setupUi(self, softwareMainWindow):
        softwareMainWindow.setObjectName("softwareMainWindow")
        softwareMainWindow.setFixedSize(630, 320)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        softwareMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.permIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        softwareMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(softwareMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLineEdit.setGeometry(QtCore.QRect(90, 40, 360, 20))
        self.queryLineEdit.setObjectName("queryLineEdit")
        self.appsListView = QtWidgets.QListView(self.centralwidget)
        self.appsListView.setGeometry(QtCore.QRect(89, 80, 360, 200))
        self.appsListView.setObjectName("appsListView")
        self.model = QtGui.QStandardItemModel()
        self.appsListView.setModel(self.model)
        self.okPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.okPushButton.setGeometry(QtCore.QRect(460, 39, 71, 22))
        self.okPushButton.setObjectName("okPushButton")
        softwareMainWindow.setCentralWidget(self.centralwidget)

        self.okPushButton.clicked.connect(self.callback)

        self.retranslateUi(softwareMainWindow)
        QtCore.QMetaObject.connectSlotsByName(softwareMainWindow)

        with open(src.paths.exportSoftwarePath, 'r') as r:
            for line in r.readlines():
                item = QtGui.QStandardItem(line)
                self.model.appendRow(item)

    def retranslateUi(self, softwareMainWindow):
        _translate = QtCore.QCoreApplication.translate
        softwareMainWindow.setWindowTitle(_translate("softwareMainWindow", "EzSetup"))
        self.okPushButton.setText(_translate("softwareMainWindow", "OK"))