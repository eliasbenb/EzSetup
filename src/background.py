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
        icon.addPixmap(QtGui.QPixmap(src.paths.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        backgroundMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(backgroundMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathLineEdit.setGeometry(QtCore.QRect(90, 40, 360, 20))
        self.pathLineEdit.setText("")
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.browsePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.browsePushButton.setGeometry(QtCore.QRect(460, 39, 71, 22))
        self.browsePushButton.setObjectName("browsePushButton")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(90, 80, 360, 200))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        backgroundMainWindow.setCentralWidget(self.centralwidget)

        self.backgroundLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.backgroundLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.backgroundLabel.setScaledContents(True)

        self.browsePushButton.clicked.connect(self.image_browse)

        self.retranslateUi(backgroundMainWindow)
        QtCore.QMetaObject.connectSlotsByName(backgroundMainWindow)

    def retranslateUi(self, backgroundMainWindow):
        _translate = QtCore.QCoreApplication.translate
        backgroundMainWindow.setWindowTitle(_translate("backgroundMainWindow", "EzSetup"))
        self.browsePushButton.setText(_translate("backgroundMainWindow", "Browse"))

    def image_browse(self):
        QFileDialog = QtWidgets.QFileDialog()
        QFilter = "Image Files (*.png *.jpg *gif *.bmp)"
        current_dir = os.getcwd()
        file_name = QtWidgets.QFileDialog.getOpenFileName(parent=QFileDialog, caption="Select Background File", directory=current_dir, filter=QFilter)
        pixmap = QtGui.QPixmap(file_name[0])
        self.backgroundLabel.setPixmap(pixmap)
        self.backgroundLabel.show()
        try:
            shutil.copy(file_name[0], src.paths.export_background_path)
        except:
            pass