##Ch05 R5.14

def subString_firstLetter(string):
    if len(string) == 0: return
#    n = len(string)
#    print(n)
    print(string)
#    string = string[0:n-1]
    string = subString_firstLetter(string[0:len(string)-1])
    return


def All_subString(string):
    if len(string) == 0: return print('*')
    subString_firstLetter(string)
    All_subString(string[1:])
    return

All_subString('Mississipi')
