from bernstein import *
from dependencyReader import *

class resolveDepenencies():
	def __init__(self, xmlDeps):
		self.obj = parseDependencies(xmlDeps)
		self.dependencies = self.obj.getParsedDep()
		self.dependencies = self.obj.getParsedDep()
		self.dependencies = separateFdj(list(self.dependencies))
		self.dependencies = delRedundancy (list(self.dependencies))
		self.dependencies = minimunFdi(list(self.dependencies))
		self.dependencies = reGroupFdi(list(self.dependencies))
		self.keys =  getKeys(list(self.dependencies))
		self.dependencies = keyInside(list(self.dependencies),self.keys)
	
	def giveDependencies(self):
		return self.dependencies
