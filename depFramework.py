"""
  <depFramework.py este script es un pequeno framework para el programa>
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


#combinacinaciones unicas con n cantidad deseada
def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

#lista unica (elemina los repetidos)
def uniqueList(seq): 
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked

#regresa todo fdj
def getFdj(dependencies):
    fdj = []
    for i in dependencies:
        temp = i["fdj"].split(",")
        for j in temp:
            fdj.append(j)
    return fdj

#si un side se encuentra dentro de una lista
def insideXlist(xlist, side):
    side = side.split(",")
    temp = 0
    answer = 0
    for x in side:
        if x in xlist:
            temp = temp + 1
    if len(side) == temp:
        answer = 1
    return answer

#de forma "array(list en python) a forma dependencia creada por diego =D" 
def ArrayToDep (xarray):
    temp = xarray[0]
    if (len(xarray) > 1):
        for x in range(1, len(xarray)):
            temp = temp + "," + xarray[x]
    return temp

#agregar dependencia al bunch
def appendDependency(dependencies, fdi, fdj):
    dependencies.append({"fdi": fdi, "fdj": fdj})
    return dependencies

#buscar items que no estan en fdj (solo en fdi)
def getNotIinJ(fdi,fdj):
        notInJ = []
        for i in fdi:
            if i not in fdj:
                notInJ.append(i)
        return notInJ

#conseguir todo fdj y fdi en modo "array"
def getDepSides(dependencies):
    fdi = []
    fdj = []
    for i in range(0,len(dependencies)):
        appendToList(fdi, dependencies[i]["fdi"])
        appendToList(fdj, dependencies[i]["fdj"])
        fdi = uniqueList(fdi)
        fdj = uniqueList(fdj)
    return fdi,fdj
        
  
def intersection(list1, list2):
    int_dict = {}
    list1_dict = {}
    for e in list1:
        list1_dict[e] = 1
    for e in list2:
        if list1_dict.has_key(e):
            int_dict[e] = 1
    return int_dict.keys()


def union(list1, list2):
    union_dict = {}
    for e in list1:
        union_dict[e] = 1
    for e in list2:
        union_dict[e] = 1
    return union_dict.keys()

#agregar a un array itemos en modo Diego 
def appendToList(xlist, newadds):
    newadds = newadds.split(",")
    for i in newadds:
        xlist.append(i)
    return xlist

