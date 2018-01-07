## Ch08 P8.18

from urllib.request import urlopen

ALL_LETTER ='abcdefghijklmnopqrstuvwxyz'
dict1 = {}
website = urlopen('https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2004.txt')
encoding = 'utf-8'
for line in website:
    line = str(line, encoding)
    #print(line)
    data = line.split(' ',1)
    data1 = data[1].strip().rsplit(' ', 1)
    dict1[data1[0].strip()] = data1[1].strip()

dict2 = {}
for letter in ALL_LETTER:
    dict2[letter]= set()
    for i in dict1:
        if i[0].lower() == letter:
            dict2[letter].add(i)

print(dict2)



userIn0 = input('please enter initial letter of country name: ')
for i in dict2[userIn0.lower()]:
    print(i)
userIn = input('please enter the name of country (enter quit to finish): ')
while userIn != 'quit':
    if userIn in dict1:
        print(dict1[userIn])
    else:
        print('Not found!')
    
    userIn0 = input('please enter initial letter of country name: ')
    for i in dict2[userIn0.lower()]:
        print(i)
    userIn = input('please enter the name of country (enter quit to finish): ')