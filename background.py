from PyQt5 import QtCore, QtGui, QtWidgets
import imagebytes, mglobals, os

class Ui_backgroundMainWindow(object):
    def setupUi(self, backgroundMainWindow):
        backgroundMainWindow.setObjectName("backgroundMainWindow")
        backgroundMainWindow.setFixedSize(630, 100)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        backgroundMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(mglobals.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        backgroundMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(backgroundMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLineEdit.setGeometry(QtCore.QRect(89, 40, 361, 20))
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.explorerToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.explorerToolButton.setGeometry(QtCore.QRect(460, 39, 71, 22))
        self.explorerToolButton.setObjectName("explorerToolButton")
        backgroundMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(backgroundMainWindow)
        QtCore.QMetaObject.connectSlotsByName(backgroundMainWindow)

    def retranslateUi(self, backgroundMainWindow):
        _translate = QtCore.QCoreApplication.translate
        backgroundMainWindow.setWindowTitle(_translate("backgroundMainWindow", "EzSetup"))
        self.fileLineEdit.setText(_translate("backgroundMainWindow", "Select background image"))
        self.explorerToolButton.setText(_translate("backgroundMainWindow", "..."))
