##Ch07 P7.14

from urllib.request import urlopen

webUrl = input('Please enter an url: ')
fileName = input('Please enter the name of file: ')
webPage = urlopen('http://' + webUrl)
outFile = open(fileName, 'w')

encoding = "utf-8"
for line in webPage:
    line = str(line, encoding)
    outFile.write(line + "\n")

webPage.close()
outFile.close()