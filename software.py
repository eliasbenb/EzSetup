from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import imagebytes, mglobals, os, requests, re, time, wgetter

class Ui_softwareMainWindow(object):
    def callback(self):
        def exported_sucess_message():
            successMessageBox = QtWidgets.QMessageBox()
            successMessageBox.setIcon(QtWidgets.QMessageBox.Information)

            successMessageBox.setText("Magnet links have been successfully exported to the local directory.")
            successMessageBox.setWindowTitle("Task Completed!")
            successMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(mglobals.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            successMessageBox.setWindowIcon(icon)
                
            successMessageBox.exec_()

        def error_message():
            errorMessageBox = QtWidgets.QMessageBox()
            errorMessageBox.setIcon(QtWidgets.QMessageBox.Information)

            errorMessageBox.setText("Something went wrong! Please inform me through GitHub!")
            errorMessageBox.setWindowTitle("Error!")
            errorMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(mglobals.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            errorMessageBox.setWindowIcon(icon)
                
            errorMessageBox.exec_()
        try:
            query = self.queryLineEdit.text()
            link = "https://en.uptodown.com/windows/search/"+query
            request = requests.get(link)
            source = request.content
            soup = BeautifulSoup(source, 'lxml')
            app_link = soup.find('a', attrs={'title': re.compile("^download")})
            app_link = app_link.get('href')
            with open(mglobals.app_list_path, 'a+') as w:
                w.write(str(app_link))
                w.write('\n')
            item = QtGui.QStandardItem(app_link)
            self.model.appendRow(item)
        except:
            error_message()

    def setupUi(self, softwareMainWindow):
        softwareMainWindow.setObjectName("softwareMainWindow")
        softwareMainWindow.setFixedSize(630, 350)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        softwareMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(mglobals.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        softwareMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(softwareMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLineEdit.setGeometry(QtCore.QRect(89, 40, 361, 20))
        self.queryLineEdit.setObjectName("queryLineEdit")
        self.appsListView = QtWidgets.QListView(self.centralwidget)
        self.appsListView.setGeometry(QtCore.QRect(89, 80, 441, 221))
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

        with open(mglobals.app_list_path, 'r') as r:
            for line in r.readlines():
                item = QtGui.QStandardItem(line)
                self.model.appendRow(item)

    def retranslateUi(self, softwareMainWindow):
        _translate = QtCore.QCoreApplication.translate
        softwareMainWindow.setWindowTitle(_translate("softwareMainWindow", "EzSetup"))
        self.okPushButton.setText(_translate("softwareMainWindow", "OK"))
