##Ch07 R7.17

try:
    outFile = open('hello1.txt', 'w')
    try:

        outFile.write(str(1.1/0))

    finally:
        outFile.close()

except IOError:
    print('Can not write the file!')

