# -*- coding: utf-8 -*-
##Ch07 P7.1

outfile = open('hello.txt', 'w')
outfile.write('Hello, World!')
outfile.close()

infile = open('Hello.txt', 'r')
text = infile.readline()
print(text)