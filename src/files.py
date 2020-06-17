from PyQt5 import QtCore, QtGui, QtWidgets
import os

import src.paths, src.imagebytes, src.qtObjects

class Ui_filesMainWindow(object):
    def setupUi(self, filesMainWindow):
        filesMainWindow.setObjectName("filesMainWindow")
        filesMainWindow.setFixedSize(630, 320)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        filesMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.permIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        filesMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(filesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browsePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.browsePushButton.setGeometry(QtCore.QRect(461, 38, 80, 23))
        self.browsePushButton.setObjectName("browsePushButton")
        self.pathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathLineEdit.setGeometry(QtCore.QRect(79, 40, 361, 20))
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 89, 461, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        filesMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(filesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(filesMainWindow)

        self.browsePushButton.clicked.connect(src.qtObjects.folder_browse)

    def retranslateUi(self, filesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        filesMainWindow.setWindowTitle(_translate("filesMainWindow", "EzSetup - Files"))
        self.browsePushButton.setText(_translate("filesMainWindow", "Browse"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("filesMainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("filesMainWindow", "Destination"))