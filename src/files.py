from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil

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

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        filesMainWindow.setCentralWidget(self.centralwidget)
        
        if os.path.exists(src.paths.importFilesListPath):
            with open(src.paths.importFilesListPath, 'r') as r:
                lines = r.readlines()
            if len(lines) > 0:
                count = 0
                while len(lines) > count:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(lines[count])))
                    self.tableWidget.resizeColumnToContents(0)
                    count = count + 1
                    self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(lines[count])))
                    self.tableWidget.resizeColumnToContents(1)
                    count = count + 1
        elif os.path.exists(src.paths.exportFilesListPath):
            with open(src.paths.exportFilesListPath, 'r') as r:
                lines = r.readlines()
            if len(lines) > 0:
                count = 0
                while len(lines) > count:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(lines[count])))
                    self.tableWidget.resizeColumnToContents(0)
                    count = count + 1
                    try:
                        self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(lines[count])))
                        self.tableWidget.resizeColumnToContents(1)
                        count = count + 1
                    except:
                        pass
        
        self.retranslateUi(filesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(filesMainWindow)

        self.browsePushButton.clicked.connect(self.folder_browse)
        self.tableWidget.cellClicked.connect(self.set_dest)

    def retranslateUi(self, filesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        filesMainWindow.setWindowTitle(_translate("filesMainWindow", "EzSetup - Files"))
        self.browsePushButton.setText(_translate("filesMainWindow", "Browse"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("filesMainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("filesMainWindow", "Destination"))

    def folder_browse(self):
        try:
            QFileDialog = QtWidgets.QFileDialog()
            current_dir = os.getcwd()
            folder_path = QtWidgets.QFileDialog.getExistingDirectory(parent=QFileDialog, caption="Select a Folder", directory=current_dir)
            dest_dir = os.path.join(src.paths.exportFilesPath,os.path.basename(folder_path))
        except:
            src.qtObjects.error_message("FILx01")
        if folder_path != '':
            try:
                self.pathLineEdit.setText(folder_path)
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(folder_path))
                self.tableWidget.resizeColumnToContents(0)
                self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(""))
            except:
                src.qtObjects.error_message("FILx02")

            with open(src.paths.exportFilesListPath, 'r') as r:
                lines = r.readlines()
            if len(lines) == 0:
                with open(src.paths.exportFilesListPath, 'a') as a:
                    a.write(folder_path)
                    a.write("\n")
            else:
                with open(src.paths.exportFilesListPath, 'a') as a:
                    a.write("\n")
                    a.write(folder_path)
                    a.write("\n")
            try:
                shutil.copytree(folder_path,dest_dir)
                src.qtObjects.success_message()
            except:
                src.qtObjects.error_message("FILx03")
        else:
            pass
    
    def set_dest(self, row, column):
        if column == 1:
            QFileDialog = QtWidgets.QFileDialog()
            current_dir = os.getcwd()
            folder_path = QtWidgets.QFileDialog.getExistingDirectory(parent=QFileDialog, caption="Select a Folder", directory=current_dir)
            self.tableWidget.setItem(row , 1, QtWidgets.QTableWidgetItem(folder_path))
            self.tableWidget.resizeColumnToContents(1)

            with open(src.paths.exportFilesListPath, 'r') as r:
                lines = r.readlines()
            if len(lines) > (2*row)+1:
                lines[(row*2)+1] = folder_path+"\n"
                with open(src.paths.exportFilesListPath, 'w') as w:
                    w.writelines( lines )
            else:
                with open(src.paths.exportFilesListPath, 'a') as a:
                    a.write(folder_path)