## Regular expression in python

# Python library of regular expression: re
import re

# re.search() method
inFile = open('romeo_and_juliet.txt', 'r', encoding = "utf8")

# find all lines containing 'Juliet'
for line in inFile:
    line = line.strip()
    if re.search('Juliet', line):
        print(line)

print()

# ^ is to match at the beginning of line
# reset file seek cursor to the beginning of the file
inFile.seek(0)

# find the lines starting with 'Juliet'
for line in inFile:
    line = line.strip()
    if re.search('^Juliet', line):
        print(line)

print()

# Search for lines that start with 'S', followed by
# 4 characters, followed by 't'
# period, '.', matches any character
inFile.seek(0)

for line in inFile:
    line = line.strip()
    if re.search('^S...t,', line):
        print(line)
        
print()
inFile.seek(0)

# notice that regex default is greedy, for * and + adding as many as possible
# below example, result is whole string, not 'Stay not,'
line = 'Stay not, be gone, live, and hereafter say, in the vault,'
print(re.findall('^S..+t,', line))
    

inFile.close()




