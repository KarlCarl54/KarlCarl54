# list utilities

def listprod(List):	# product of list elements
    prod = 1
    for v in List:
        prod *= v
    return prod

def Kmult(K,List): # multiply a list by a scalar K
    return [x*K for x in List]

def Ksum(K,List): # add scalar K to a list
    return [x+K for x in List]

def NotZero(List): # return True for nonzero elements in a list
    return [x!=0 for x in List]

def elbyelsum(List1,List2): # element by element sum of two lists
    return [List1[i]+List2[i] for i in range(min(len(List1),len(List2)))]

def elbyeldiff(List1,List2): # element by element difference of two lists
    return [List1[i]-List2[i] for i in range(min(len(List1),len(List2)))]

def elbyelprod(List1,List2): # element by element product of two lists
    return [List1[i]*List2[i] for i in range(min(len(List1),len(List2)))]

def elbyelquot(List1,List2): # element by element quotient of two lists
    return [List1[i]/List2[i] for i in range(min(len(List1),len(List2)))]

def getindex(inlist,val):
# index returns an error if the value does not exist
# so rather than deal with the error, return empty
    return inlist.index(val) if val in inlist else []

def valremove(inlist,val)
# remove a value from a list if it exists
    inlist.remove(val) if val in inlist else []

def lastidx(List,value): # find last index of value in List
    RList = List[::-1] # slicing
    return len(List)-1-RList.index(value)

def findall(List,value): # find all indices of value in List
    return [idx for idx in range(len(List)) if List[idx]==value]

