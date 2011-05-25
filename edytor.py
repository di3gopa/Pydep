# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edytor.ui'
#
# Created: Thu Jun  4 19:06:01 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(834, 632)
        self.openButton = QtGui.QPushButton(Form)
        self.openButton.setGeometry(QtCore.QRect(620, 20, 141, 31))
        self.openButton.setObjectName("openButton")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 30, 161, 16))
        self.label.setObjectName("label")
        self.label_opened = QtGui.QLabel(Form)
        self.label_opened.setGeometry(QtCore.QRect(210, 26, 381, 20))
        self.label_opened.setObjectName("label_opened")
        self.pushButton_resolve = QtGui.QPushButton(Form)
        self.pushButton_resolve.setGeometry(QtCore.QRect(40, 60, 171, 27))
        self.pushButton_resolve.setObjectName("pushButton_resolve")
        self.editor_window = QtGui.QTextEdit(Form)
        self.editor_window.setGeometry(QtCore.QRect(20, 110, 791, 501))
        self.editor_window.setObjectName("editor_window")
        self.pushButton_save = QtGui.QPushButton(Form)
        self.pushButton_save.setEnabled(False)
        self.pushButton_save.setGeometry(QtCore.QRect(620, 60, 141, 31))
        self.pushButton_save.setObjectName("pushButton_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "pyDep", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Archivo para Analizar:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_resolve.setText(QtGui.QApplication.translate("Form", "Resolver Dependencias", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("Form", "Guardar", None, QtGui.QApplication.UnicodeUTF8))

