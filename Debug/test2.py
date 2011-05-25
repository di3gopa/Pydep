def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def uniqueList(seq): 
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked

def appendDependency(dependencies, fdi, fdj):
    dependencies.append({"fdi": fdi, "fdj": fdj})
    return dependencies

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

def appendToList(xlist, newadds):
    newadds = newadds.split(",")
    for i in newadds:
        xlist.append(i)
    return xlist

def xclosure (who, dependencies):
    xlistold = []
    xlist = []
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
    return xlist          

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


def xclosureOld (who, dependencies):
    xlistold = []
    xlist = []
    xlist = appendToList(list(xlist), dependencies[who]["fdi"])
    dependencies.pop(who)
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
    return xlist       

def delRedundancyOld (dependencies):
    i = 0
    deplen = len(dependencies)
    dependencies = dependencies
    while (i < len(dependencies)):
        xlist = xclosureOld(i, list(dependencies))
        if dependencies[i]["fdj"] in xlist:
            dependencies.pop(i)
        else:
            i = i+1
    return dependencies

def ArrayToDep (xarray):
    temp = xarray[0]
    if (len(xarray) > 1):
        for x in range(1, len(xarray)):
            temp = temp + "," + xarray[x]
    return temp

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
                tempXclosure = xclosure(tempDep(i),list(tempDep))
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

def getFdj(dependencies):
    fdj = []
    for i in dependencies:
        temp = i["fdj"].split(",")
        for j in temp:
            fdj.append(j)
    return fdj


    
def getKeys(dependencies):
    fdj = getFdj(list(dependencies))
    fdj = uniqueList(fdj)
    fdj.sort()
    numberslist = []
    for i in range (0, len(dependencies)):
        numberslist.append(i)
    for i in range (0, len(dependencies)):
        closures = []
        fullClosure = []
        permutations = xuniqueCombinations(numberslist, i+1)
        for uc in permutations:
            
            for x in uc:
                closures.append(xclosure(x, list(dependencies)))
                tempfdj = list(fdj) + dependencies[x]["fdi"].split(",")
            for x in closures:
                fullClosure = fullClosure + x
            fullClosure = uniqueList(list(fullClosure))
            tempfdj.sort()
            fullClosure.sort()
            if tempfdj == fullClosure:
                return uc
            del(tempfdj[:])
            del(closures[:])
            
        

dependencies = []
"""dependencies = appendDependency(dependencies, "a,b", "y,x")
dependencies = appendDependency(dependencies, "c,x,t", "m")
dependencies = appendDependency(dependencies, "m", "a")
dependencies = appendDependency(dependencies, "x", "t,b")"""
dependencies = appendDependency(dependencies, "t,a", "x")
dependencies = appendDependency(dependencies, "b", "z,l")
dependencies = appendDependency(dependencies, "z", "m")
dependencies = appendDependency(dependencies, "a", "x,l")
dependencies = appendDependency(dependencies, "x,t", "b,p")


"""dependencies = separateFdj(list(dependencies))"""
dependenciesOld = list(dependencies)
dependencies = delRedundancy (list(dependencies))
dependenciesOld = delRedundancyOld (list(dependenciesOld))
dependencies = minimunFdi(list(dependencies))    




