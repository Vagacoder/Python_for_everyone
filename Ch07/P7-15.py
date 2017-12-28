##Ch07 P7.15

from urllib.request import urlopen

#web = urlopen('http://wfs.sbcc.edu/student/qhu/cs111_Hu_Qi/A12-FinalProject/index.html')

web = urlopen('http://www.guancha.cn/')
encoding = 'utf-8'

urlList = []


for line in web:
    if len(urlList) >=100:
        break
    line = str(line, encoding)
    print(line)
    key = 'href=\"'
    if key in line:
        start = line.index(key) + len(key)
        end = line.index('\"', start)
        urlList.append(line[start: end])

web.close()

print('============')
print(urlList)

outFile = open('guanchaURL.txt', 'w')
for line in urlList:
    outFile.write(line + '\n')

outFile.close()