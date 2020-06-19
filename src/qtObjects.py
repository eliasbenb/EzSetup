from PyQt5 import QtWidgets, QtGui

import src.paths, src.imagebytes

def success_message():
    successMessageBox = QtWidgets.QMessageBox()
    successMessageBox.setIcon(QtWidgets.QMessageBox.Information)

    successMessageBox.setText("Task Completed Successfully!")
    successMessageBox.setWindowTitle("Task Completed!")
    successMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(src.paths.permIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    successMessageBox.setWindowIcon(icon)
        
    successMessageBox.exec_()

def error_message(error_code):
    errorMessageBox = QtWidgets.QMessageBox()
    errorMessageBox.setIcon(QtWidgets.QMessageBox.Information)

    errorMessageBox.setText("Something went wrong! Please inform me through GitHub! Error Code: "+error_code)
    errorMessageBox.setWindowTitle("Error!")
    errorMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(src.paths.permIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    errorMessageBox.setWindowIcon(icon)
        
    errorMessageBox.exec_()