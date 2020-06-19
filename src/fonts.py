from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil
from fontmeta import FontMeta

import src.paths, src.imagebytes, src.qtObjects

class Ui_fontsMainWindow(object):
    def setupUi(self, fontsMainWindow):
        fontsMainWindow.setObjectName("fontsMainWindow")
        fontsMainWindow.setFixedSize(630, 320)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        fontsMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.paths.permIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fontsMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(fontsMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathLineEdit.setGeometry(QtCore.QRect(79, 40, 361, 20))
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.browsePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.browsePushButton.setGeometry(QtCore.QRect(461, 38, 80, 23))
        self.browsePushButton.setObjectName("browsePushButton")
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
        fontsMainWindow.setCentralWidget(self.centralwidget)

        if os.path.exists(src.paths.importFontsListPath):
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
        elif os.path.exists(src.paths.exportFontsListPath):
            with open(src.paths.exportFontsListPath, 'r') as r:
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

        self.browsePushButton.clicked.connect(self.font_browse)

        self.retranslateUi(fontsMainWindow)
        QtCore.QMetaObject.connectSlotsByName(fontsMainWindow)

    def retranslateUi(self, fontsMainWindow):
        _translate = QtCore.QCoreApplication.translate
        fontsMainWindow.setWindowTitle(_translate("fontsMainWindow", "EzSetup - Fonts"))
        self.browsePushButton.setText(_translate("fontsMainWindow", "Browse"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("fontsMainWindow", "Font Family"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("fontsMainWindow", "Font Subfamily"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("fontsMainWindow", "Font Designer"))

    def font_browse(self):
        try:
            QFileDialog = QtWidgets.QFileDialog()
            QFilter = "Font Files (*.otf *.ttf)"
            current_dir = os.getcwd()
            file_name = QtWidgets.QFileDialog.getOpenFileName(parent=QFileDialog, caption="Select Font File", directory=current_dir, filter=QFilter)
        except:
            src.qtObjects.error_message("FNTx01")
        if file_name[0] != '':
            try:
                shutil.copy(file_name[0], src.paths.exportFontsPath)
            except:
                src.qtObjects.error_message("FNTx02")
            try:
                font_meta = FontMeta(file_name[0])
                font_meta = font_meta.get_data()
            except:
                src.qtObjects.error_message("FNTx03")
            try:
                font_family = font_meta["font_family"]
            except:
                font_family = "N/A"
            try:
                font_subamily = font_meta["subfamily"]
            except:
                font_subamily = "N/A"
            try:
                font_designer = font_meta["designer"]
            except:
                font_designer = "N/A"

            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(font_family))
            self.tableWidget.resizeColumnToContents(0)
            self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(font_subamily))
            self.tableWidget.resizeColumnToContents(1)
            self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(font_designer))
            self.tableWidget.resizeColumnToContents(2)
            self.pathLineEdit.setText(file_name[0])
            try:
                with open(src.paths.exportFontsListPath, 'a') as a:
                    a.write(font_family+"\n"+font_subamily+"\n"+font_designer+"\n")
                src.qtObjects.success_message()
            except:
                src.qtObjects.error_message("FNTx04")