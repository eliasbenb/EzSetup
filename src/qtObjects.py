from PyQt5 import QtWidgets, QtGui
import os, shutil, zipfile

import src.paths, src.imagebytes

def success_message():
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
    dest_dir = os.path.join(src.paths.export_files_path,os.path.basename(folder_path))
    try:
        shutil.copytree(folder_path,dest_dir)
        success_message()
    except:
        error_message()

def file_browse():
    QFileDialog = QtWidgets.QFileDialog()
    QFilter = "EzSetup File (*.ez)"
    current_dir = os.getcwd()
    file_name = QtWidgets.QFileDialog.getOpenFileName(parent=QFileDialog, caption="Select File", directory=current_dir, filter=QFilter)
    try:
        with zipfile.ZipFile(file_name[0], 'r') as zipObject:
            zipObject.extractall(src.paths.import_path)
        success_message()
    except:
        error_message()

def image_browse():
    QFileDialog = QtWidgets.QFileDialog()
    QFilter = "Image Files (*.png *.jpg *gif *.bmp)"
    current_dir = os.getcwd()
    file_name = QtWidgets.QFileDialog.getOpenFileName(parent=QFileDialog, caption="Select Background File", directory=current_dir, filter=QFilter)
    pixmap = QtGui.QPixmap(file_name[0])
    try:
        shutil.copy(file_name[0], src.paths.export_background_path)
        success_message()
    except:
        error_message()
    return(pixmap)