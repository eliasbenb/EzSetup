from PyQt5 import QtWidgets, QtGui
import os, shutil

import src.paths, src.imagebytes

def sucess_message():
    successMessageBox = QtWidgets.QMessageBox()
    successMessageBox.setIcon(QtWidgets.QMessageBox.Information)

    successMessageBox.setText("Task Completed Successfully!")
    successMessageBox.setWindowTitle("Task Completed!")
    successMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(src.paths.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    successMessageBox.setWindowIcon(icon)
        
    successMessageBox.exec_()

def error_message():
    errorMessageBox = QtWidgets.QMessageBox()
    errorMessageBox.setIcon(QtWidgets.QMessageBox.Information)

    errorMessageBox.setText("Something went wrong! Please inform me through GitHub!")
    errorMessageBox.setWindowTitle("Error!")
    errorMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(src.paths.icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    errorMessageBox.setWindowIcon(icon)
        
    errorMessageBox.exec_()

def folder_browse():
    QFileDialog = QtWidgets.QFileDialog()
    current_dir = os.getcwd()
    folder_path = QtWidgets.QFileDialog.getExistingDirectory(parent=QFileDialog, caption="Select a Folder", directory=current_dir)
    dest_dir = os.path.join(src.paths.files_path,os.path.basename(folder_path))
    try:
        shutil.copytree(folder_path,dest_dir)
        sucess_message()
    except:
        error_message()

def image_browse():
    QFileDialog = QtWidgets.QFileDialog()
    QFilter = "Image Files (*.png *.jpg *gif *.bmp)"
    current_dir = os.getcwd()
    file_name = QtWidgets.QFileDialog.getOpenFileName(parent=QFileDialog, caption="Select Background File", directory=current_dir, filter=QFilter)
    try:
        shutil.copy(file_name[0], src.paths.background_path)
        sucess_message()
    except:
        error_message()