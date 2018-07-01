import re

def examin(formulaReplaced):
    formulaSplit = re.split("\+|=", formulaReplaced)
    augend = formulaSplit[0].strip()
    addend = formulaSplit[1].strip()
    result = formulaSplit[2].strip()
    if augend.isdigit() and addend.isdigit() and result.isdigit():
        return int(augend) + int(addend) == int(result)
    else:
        return False


print(examin('3000 + 400 = 3400'))