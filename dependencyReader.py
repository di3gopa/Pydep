"""
  <dependencyReader.py este script parsea las dependencias dadas en formato xml>
    Copyleft (C) 2009  Diego Tejera

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
  
"""

import libxml2

class parseDependencies ():
    def __init__(self, deps):
        self.doc = libxml2.parseDoc(deps)
        self.root = self.doc.children
        self.child = self.root.children
        self.dependencies = []
        self.parseDepXML()
        
        
    def parseDepXML(self):
        i = 0
        child = self.child
        
        while child is not None:
            if child.type == "element":
                if child.name == "dependency":
                    self.dependencies.append({"fdi": None, "fdj": None})
                    Attributes = child.children
                    while Attributes is not None:
                        if Attributes.type == "element":
                            if Attributes.name == "fdi":
                                self.dependencies[i]["fdi"] = Attributes.content
                            elif Attributes.name == "fdj":
                                self.dependencies[i]["fdj"] = Attributes.content
                        Attributes = Attributes.next
                i = i+1    
            child = child.next

    def getParsedDep(self):
        return self.dependencies
