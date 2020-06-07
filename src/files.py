from PyQt5 import QtCore, QtGui, QtWidgets
from distutils.dir_util import copy_tree
import os

import src.paths, src.imagebytes, src.qtObjects

class Ui_filesMainWindow(object):
    def setupUi(self, filesMainWindow):
        filesMainWindow.setObjectName("filesMainWindow")
        filesMainWindow.setFixedSize(630, 350)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        filesMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        filesMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(filesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLineEdit.setGeometry(QtCore.QRect(89, 40, 361, 20))
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.filesListView = QtWidgets.QListView(self.centralwidget)
        self.filesListView.setGeometry(QtCore.QRect(89, 80, 441, 221))
        self.filesListView.setObjectName("filesListView")
        self.explorerToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.explorerToolButton.setGeometry(QtCore.QRect(460, 39, 71, 22))
        self.explorerToolButton.setObjectName("explorerToolButton")
        filesMainWindow.setCentralWidget(self.centralwidget)

        self.explorerToolButton.clicked.connect(src.qtObjects.folder_browse)

        self.retranslateUi(filesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(filesMainWindow)

    def retranslateUi(self, filesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        filesMainWindow.setWindowTitle(_translate("filesMainWindow", "EzSetup"))
        self.fileLineEdit.setText(_translate("filesMainWindow", "Select file/folder"))
        self.explorerToolButton.setText(_translate("filesMainWindow", "..."))