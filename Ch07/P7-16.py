## Ch07 P7.16


from urllib.request import urlopen


web = urlopen('http://www.guancha.cn')

header = web.headers['content-type']

encoding = ''
found = False

if 'charset' in header:
    if 'charset=' in header:
        start = header.index('charset=')+ len('charset=')
        end = header.index('\>')
        encoding = header[start:end].strip()
        found = True

    elif 'charset =' in header:
        start = header.index('charset =')+ len('charset =')
        end = header.index('\>')
        encoding = header[start:end].strip()
        found = True

else:

    first3Bytes = web.read(3)
    #print(first3Bytes)
    if (first3Bytes[0], first3Bytes[1], first3Bytes[2]) == (239, 187, 191):
        encoding = 'utf-8'
        found = True
    elif (first3Bytes[0], first3Bytes[1]) == (254, 255) or (first3Bytes[0], first3Bytes[1]) == (255, 254):
        encoding = 'utf-16'
        found = True

    if not found:

        for line in web:
            line = str(line, 'latin_1')
            #print(line)
            if 'encoding' in line:
                if 'encoding=' in line:
                    start = line.index('encoding=') + len('encoding=')
                    end = line.index('>')
                    encoding = line[start:end].strip('\"')
                    found = True
                    break
                elif 'encoding =' in line:
                    start = line.index('encoding =') + len('encoding =')
                    end = line.index('>')
                    encoding = line[start:end].strip('\"')
                    found = True
                    break

            elif 'charset' in line:
                if 'charset=' in line:
                    start = line.index('charset=') + len('charset=')
                    end = line.index('>')
                    encoding = line[start:end].strip('\"')
                    found = True
                    break

                elif 'charset =' in line:
                    start = line.index('charset =') + len('charset =')
                    end = line.index('>')
                    encoding = line[start:end].strip('\"')
                    found = True
                    break


if not found:
    print('No encoding found!')

else:
    print(encoding)

web.close()


