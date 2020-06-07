from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil

import src.paths, src.imagebytes, src.qtObjects

class Ui_backgroundMainWindow(object):
    def setupUi(self, backgroundMainWindow):
        backgroundMainWindow.setObjectName("backgroundMainWindow")
        backgroundMainWindow.resize(630, 100)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        backgroundMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        backgroundMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(backgroundMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLineEdit.setGeometry(QtCore.QRect(89, 40, 361, 20))
        self.fileLineEdit.setText("")
        self.fileLineEdit.setReadOnly(True)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.browsePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.browsePushButton.setGeometry(QtCore.QRect(460, 39, 71, 22))
        self.browsePushButton.setObjectName("browsePushButton")
        backgroundMainWindow.setCentralWidget(self.centralwidget)

        self.browsePushButton.clicked.connect(src.qtObjects.image_browse)

        self.retranslateUi(backgroundMainWindow)
        QtCore.QMetaObject.connectSlotsByName(backgroundMainWindow)

    def retranslateUi(self, backgroundMainWindow):
        _translate = QtCore.QCoreApplication.translate
        backgroundMainWindow.setWindowTitle(_translate("backgroundMainWindow", "EzSetup"))
        self.browsePushButton.setText(_translate("backgroundMainWindow", "Browse"))