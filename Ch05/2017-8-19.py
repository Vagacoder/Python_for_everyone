##Ch05 R5.14

def subString_firstLetter(string):
    if len(string) == 0: 
        return
    else:
        print(string)
        string = subString_firstLetter(string[0:len(string)-1])



def All_subString(string):
    if len(string) == 0: 
        print('*')

    else:
        subString_firstLetter(string)
        All_subString(string[1:])


All_subString('Foxbat')
