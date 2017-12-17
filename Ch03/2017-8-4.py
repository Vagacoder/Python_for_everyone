## Ch03 P3.30

name = input('Please enter the name of country: ')

except_list1 = 'Belize Cambodge Mexique Mozanbique Zaire Zimbabwe'
except_list2 = 'Etats-Unis Pays-Bas'

if name.endswith('e'):
    article = 'la'
    if name in except_list1:
        article = 'le'
else:
    article = 'le'

if name[0] == 'A' or name[0] == 'E' or name[0] == 'I' or name[0] == 'O' or name[0] == 'U':
    article ="l\'"

if name in except_list2:
    article = 'les'

print(article + ' ' + name)
