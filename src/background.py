from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil

import src.paths, src.imagebytes, src.qtObjects

class Ui_backgroundMainWindow(object):
    def setupUi(self, backgroundMainWindow):
        backgroundMainWindow.setObjectName("backgroundMainWindow")
        backgroundMainWindow.setFixedSize(630, 320)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        backgroundMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.permIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        backgroundMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(backgroundMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browsePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.browsePushButton.setGeometry(QtCore.QRect(471, 38, 80, 23))
        self.browsePushButton.setObjectName("browsePushButton")
        self.pathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathLineEdit.setGeometry(QtCore.QRect(89, 40, 361, 20))
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.leftLine = QtWidgets.QFrame(self.centralwidget)
        self.leftLine.setGeometry(QtCore.QRect(81, 90, 20, 200))
        self.leftLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.leftLine.setLineWidth(1)
        self.leftLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.leftLine.setObjectName("leftLine")
        self.rightLine = QtWidgets.QFrame(self.centralwidget)
        self.rightLine.setGeometry(QtCore.QRect(439, 90, 20, 200))
        self.rightLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rightLine.setLineWidth(1)
        self.rightLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.rightLine.setObjectName("rightLine")
        self.topLine = QtWidgets.QFrame(self.centralwidget)
        self.topLine.setGeometry(QtCore.QRect(90, 81, 360, 16))
        self.topLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.topLine.setLineWidth(1)
        self.topLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topLine.setObjectName("topLine")
        self.bottomLine = QtWidgets.QFrame(self.centralwidget)
        self.bottomLine.setGeometry(QtCore.QRect(90, 281, 360, 16))
        self.bottomLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bottomLine.setLineWidth(1)
        self.bottomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottomLine.setObjectName("bottomLine")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(92, 90, 357, 201))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        backgroundMainWindow.setCentralWidget(self.centralwidget)

        self.backgroundLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.backgroundLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.backgroundLabel.setScaledContents(True)

        self.browsePushButton.clicked.connect(self.image_browse)

        if os.path.exists(src.paths.importBackgroundPath):
            pixmap = QtGui.QPixmap(src.paths.importBackgroundPath)
            self.pathLineEdit.setText(src.paths.importBackgroundPath)
            self.backgroundLabel.setPixmap(pixmap)
        elif os.path.exists(src.paths.exportBackgroundPath):
            pixmap = QtGui.QPixmap(src.paths.exportBackgroundPath)
            with open(src.paths.exportBackgroundSourcePath, 'r') as r:
                source_path = r.read()
            self.pathLineEdit.setText(source_path)
            self.backgroundLabel.setPixmap(pixmap)

        self.retranslateUi(backgroundMainWindow)
        QtCore.QMetaObject.connectSlotsByName(backgroundMainWindow)

    def retranslateUi(self, backgroundMainWindow):
        _translate = QtCore.QCoreApplication.translate
        backgroundMainWindow.setWindowTitle(_translate("backgroundMainWindow", "EzSetup - Background"))
        self.browsePushButton.setText(_translate("backgroundMainWindow", "Browse"))

    def image_browse(self):
        try:
            QFileDialog = QtWidgets.QFileDialog()
            QFilter = "Image Files (*.png *.jpg *gif *.bmp)"
            current_dir = os.getcwd()
            file_name = QtWidgets.QFileDialog.getOpenFileName(parent=QFileDialog, caption="Select Background File", directory=current_dir, filter=QFilter)
        except:
            src.qtObjects.error_message("BGx01")
        if file_name[0] != '':
            try:
                pixmap = QtGui.QPixmap(file_name[0])
                self.backgroundLabel.setPixmap(pixmap)
            except:
                pass
            try:
                shutil.copy(file_name[0], src.paths.exportBackgroundPath)
                self.backgroundLabel.show()
                src.qtObjects.success_message()
            except:
                src.qtObjects.error_message("BGx02")
            with open(src.paths.exportBackgroundSourcePath, 'w') as w:
                pass
                w.write(file_name[0])
            self.pathLineEdit.setText(file_name[0])