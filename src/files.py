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
        icon.addPixmap(QtGui.QPixmap(src.paths.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        filesMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(filesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filesListView = QtWidgets.QListView(self.centralwidget)
        self.filesListView.setGeometry(QtCore.QRect(89, 80, 360, 200))
        self.filesListView.setObjectName("filesListView")
        self.pathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathLineEdit.setGeometry(QtCore.QRect(90, 40, 360, 20))
        self.pathLineEdit.setText("")
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.browsePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.browsePushButton.setGeometry(QtCore.QRect(460, 39, 71, 22))
        self.browsePushButton.setObjectName("browsePushButton")
        filesMainWindow.setCentralWidget(self.centralwidget)

        self.browsePushButton.clicked.connect(src.qtObjects.folder_browse)

        self.retranslateUi(filesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(filesMainWindow)

    def retranslateUi(self, filesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        filesMainWindow.setWindowTitle(_translate("filesMainWindow", "EzSetup"))
        self.browsePushButton.setText(_translate("filesMainWindow", "Browse"))