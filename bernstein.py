"""
  <xclosure.py este script contiene las funciones basicas del algoritmo de bernstein>
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

from depFramework import *

def xclosure (who, dependencies, key = 0):
    xlistold = []
    xlist = []
    if (key):
        xlist = who
    else:
        xlist = appendToList(list(xlist), who["fdi"])
    m = 0
    while (xlist != xlistold):
        xlistold = list(xlist)
        j = 0
        for i in dependencies:
            if(insideXlist(list(xlist), i["fdi"])):
                xlist = appendToList(list(xlist), i["fdj"])
                dependencies.pop(j)
                xlist.sort()
            j = j+1
    xlist = uniqueList(list(xlist))
    return xlist                

#separar el lado derecho
def separateFdj (dependencies):
    deplen = len(dependencies)
    i = 0
    while (i < deplen):
        fdjs = dependencies[i]["fdj"].split(",")
        fdi = dependencies[i]["fdi"]
        if (len(fdjs) > 1):
            dependencies.pop(i)
            for j in fdjs:
                dependencies = appendDependency(dependencies, fdi, j)
        else:
            i = i+1
    return dependencies

#Elimina la redundancia de los fdi
def delRedundancy (dependencies):
    i = 0
    deplen = len(dependencies)
    while (i < len(dependencies)):
        depInAction = list(dependencies)
        who = depInAction.pop(i)
        xlist = xclosure(who, list(depInAction))
        if dependencies[i]["fdj"] in xlist:
            dependencies.pop(i)
        else:
            i = i+1
    return dependencies

#obtiene el minimo fdi
def minimunFdi (dependencies):
    for i in range(0, len(dependencies)):
        fullClosure = xclosure(dependencies[i], list(dependencies))
        fullClosure.sort()
        fullClosure = uniqueList(fullClosure)
        stop = 0
        for n in range(0, len(dependencies[i]["fdi"].split(","))):
            permutations = xuniqueCombinations(dependencies[i]["fdi"].split(","), n+1)
            for uc in permutations:
                perm = ArrayToDep(list(uc))
                tempDep = list(dependencies)
                temp = tempDep[i]["fdi"]
                tempDep[i]["fdi"] = perm
                tempXclosure = xclosure(tempDep[i],list(tempDep))
                tempXclosure.sort()
                tempXclosure = uniqueList(tempXclosure) 
                if (tempXclosure == fullClosure):
                    dependencies[i]["fdi"] = perm
                    stop = 1
                else:
                    tempDep[i]["fdi"] = temp
                if (stop):
                    break
            if (stop):
                break
    return dependencies

#obtener la superllave
def getKeys(dependencies):
    keys = []
    fdi,fdj = getDepSides(dependencies)
    keys = getNotIinJ(list(fdi), list(fdj))
    bothsides = intersection(fdi,fdj)
    all = union(fdi,fdj); all.sort()
    
    for i in range (0, len(bothsides)):
        permutations = xuniqueCombinations(bothsides, i+1)
        for uc in permutations:
            candidateKey = keys + uc
            tempXclosure = xclosure(list(candidateKey), list(dependencies), 1)
            tempXclosure.sort()
            if (tempXclosure == all):
                return candidateKey
            
#Reagrupar los fdi separados x->a x->b  a  x->a,b
def reGroupFdi(dependencies):
    for i in range(0, len(dependencies)):
    	j = i+1
        while (j < len(dependencies)):
		        if (dependencies[i]["fdi"] == dependencies[j]["fdi"]):
		            tempFdi = dependencies[i]["fdi"]
		            tempFdj = dependencies[i]["fdj"] + "," +dependencies[j]["fdj"]
		            dependencies.pop(i)
		            dependencies.pop(j-1)
		            tempDep = {"fdi": tempFdi, "fdj": tempFdj}
		            dependencies.append(tempDep)
		            j = i
		        j += 1
    return dependencies

def keyInside(dependencies,keys):
	keys = ArrayToDep(list(keys))
	for x in dependencies:
		if (x == keys):
			return dependencies
	dependencies.append({"fdi":keys,"fdj":keys})
	return dependencies  
     
