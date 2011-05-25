import sys
from PyQt4 import QtCore, QtGui
from results import Ui_Results


class StartResultWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Results()
		self.ui.setupUi(self)
		a = QtGui.QTreeWidgetItem(self.ui.treeWidget)
	def addTable(self,key,columns):
		table = QtGui.QTreeWidgetItem(self.ui.treeWidget)
		table.setText(0, key)
		table.setText(1, columns)
		
