from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import os, requests, json

import src.paths, src.imagebytes, src.qtObjects

class Ui_softwareMainWindow(object):
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
        self.searchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QtCore.QRect(461, 38, 80, 23))
        self.searchPushButton.setObjectName("searchPushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 89, 461, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.queryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLineEdit.setGeometry(QtCore.QRect(79, 40, 361, 20))
        self.queryLineEdit.setReadOnly(False)
        self.queryLineEdit.setObjectName("queryLineEdit")
        softwareMainWindow.setCentralWidget(self.centralwidget)

        self.searchPushButton.clicked.connect(self.search_button)

        if os.path.exists(src.paths.importSoftwareListPath):
            with open(src.paths.importFontsListPath, 'r') as r:
                lines = r.readlines()
            if len(lines) > 0:
                count = 0
                while len(lines) > count:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(lines[count])))
                    count = count + 1
                    self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(lines[count])))
                    count = count + 1
                    self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(lines[count])))
                    count = count + 1
                self.tableWidget.resizeColumnToContents(0)
                self.tableWidget.resizeColumnToContents(1)
                self.tableWidget.resizeColumnToContents(2)
        elif os.path.exists(src.paths.exportSoftwareListPath):
            with open(src.paths.exportSoftwareListPath, 'r') as r:
                lines = r.readlines()
            if len(lines) > 0:
                count = 0
                while len(lines) > count:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(lines[count])))
                    count = count + 1
                    self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(lines[count])))
                    count = count + 1
                    self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(lines[count])))
                    count = count + 1
                self.tableWidget.resizeColumnToContents(0)
                self.tableWidget.resizeColumnToContents(1)
                self.tableWidget.resizeColumnToContents(2)

        self.retranslateUi(softwareMainWindow)
        QtCore.QMetaObject.connectSlotsByName(softwareMainWindow)

    def retranslateUi(self, softwareMainWindow):
        _translate = QtCore.QCoreApplication.translate
        softwareMainWindow.setWindowTitle(_translate("softwareMainWindow", "EzSetup - Software"))
        self.searchPushButton.setText(_translate("softwareMainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("softwareMainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("softwareMainWindow", "Author"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("softwareMainWindow", "Latest Version"))

    def search_button(self):
        query = self.queryLineEdit.text()
        if query.startswith("https://filehippo.com") or query.startswith("http://filehippo.com") or query.startswith("www.filehippo.com") or query.startswith("filehippo.com"):
            link = query
        else:
            try:
                search_link = "https://filehippo.com/search/?q="+query
                request = requests.get(search_link)
                source = request.text
                soup = BeautifulSoup(source, 'html.parser')
                link = soup.findAll('a', class_="card-program", attrs={'data-ua':'card-program-item'})
                link = link[0].get('href')
            except:
                src.qtObjects.error_message("SOFx01")
        
        request = requests.get(link)
        source = request.text
        soup = BeautifulSoup(source, 'html.parser')
        scripts_soup = soup.find('script', type='application/ld+json')
        scipts_dict = json.loads(scripts_soup.string)
        
        software_name = scipts_dict['name']
        software_author = (soup.find('a', attrs={'data-qa':'program-developer'})).get('title')
        software_latest_version = scipts_dict['softwareVersion']

        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(software_name))
        self.tableWidget.resizeColumnToContents(0)
        self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(software_author))
        self.tableWidget.resizeColumnToContents(1)
        self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(software_latest_version))
        self.tableWidget.resizeColumnToContents(2)

        with open(src.paths.exportSoftwareListPath, 'a') as a:
            a.write(software_name)
            a.write("\n")
            a.write(software_author)
            a.write("\n")
            a.write(software_latest_version)
            a.write("\n")
        with open(src.paths.exportSoftwareLinksPath, 'a') as a:
            a.write(link)
            a.write("\n")