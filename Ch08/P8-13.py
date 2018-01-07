## Ch08 P8.13

# =============================================================================
# define main method, testinf functions of union, 
# =============================================================================
def main():
    multiset1 = {'apple':3, 'banana':2, 'grape':5}
    multiset2 = {'apple':4, 'banana':1}
    
    print(union(multiset2, multiset1))
    print(intersection(multiset1, multiset2))
    print(difference(multiset2, multiset1))
    

# =============================================================================
# define function of union
# @para dict1 first input dictionary 
# @para dict2 second input dictionary
# =============================================================================
def union(dict1, dict2):
    newDict = {}
    for i in dict1:
        newItem = dict1[i] + dict2.get(i, 0)
        newDict[i] = newItem
    
    for i in dict2:
        if i not in newDict:
            newDict[i] = dict2[i]
            
    return newDict

# =============================================================================
# define function of intersection
# @para dict1 first input dictionary 
# @para dict2 second input dictionary    
# =============================================================================
def intersection(dict1, dict2):
    newDict = {}
    for i in dict1:
        newDict[i] = min(dict1[i], dict2.get(i, 0))

    for i in dict2:
        if i not in newDict:
            newDict[i] = 0
            
    return newDict

# =============================================================================
# define function of difference
# @para dict1 first input dictionary 
# @para dict2 second input dictionary
# =============================================================================
def difference(dict1, dict2):
    newDict = {}
    for i in dict1:
        newDict[i] = abs(dict1[i] - dict2.get(i, 0))

    for i in dict2:
        if i not in newDict:
            newDict[i] = dict2[i]
            
    return newDict



main()