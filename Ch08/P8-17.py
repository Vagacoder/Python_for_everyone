## Ch08 P8.17

from urllib.request import urlopen

dict1 = {}
website = urlopen('https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2004.txt')
encoding = 'utf-8'
for line in website:
    line = str(line, encoding)
    #print(line)
    data = line.split(' ',1)
    data1 = data[1].strip().rsplit(' ', 1)
    dict1[data1[0].strip()] = data1[1].strip()

for item in dict1:
    print(item, dict1[item])

userIn = input('please enter the name of country (enter quit to finish): ')
while userIn != 'quit':
    if userIn in dict1:
        print(dict1[userIn])
    else:
        print('Not found!')
    
    userIn = input('please enter the name of country (enter quit to finish): ')