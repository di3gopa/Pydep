# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created: Thu Jun  4 20:55:38 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(920, 555)
        self.treeWidget = QtGui.QTreeWidget(Results)
        self.treeWidget.setGeometry(QtCore.QRect(10, 40, 891, 491))
        self.treeWidget.setObjectName("treeWidget")
        self.label = QtGui.QLabel(Results)
        self.label.setGeometry(QtCore.QRect(20, 17, 711, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        Results.setWindowTitle(QtGui.QApplication.translate("Results", "Respuestas - pyDep", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Results", "Llave", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Results", "Columnas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Results", "Recomendacion de Tablas para las dependencias Resueltas:", None, QtGui.QApplication.UnicodeUTF8))

