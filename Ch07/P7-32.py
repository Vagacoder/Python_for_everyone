## Ch07 P7.23

from math import *

try:
    inFile = open('params.txt', 'r')
    line = inFile.readline()

    try:
        data = line.split(',')
        B = float(data[0].strip())
        R = float(data[1].strip())
        C = float(data[2].strip())
        startTime = int(data[3].strip())
        endTime = int(data[4].strip())
        intervalTime = (endTime - startTime)/100
        time = startTime

        try:

            outFile = open('rc.txt', 'w')
            outFile.write('Time(us) Voltage(volts)\n')
            for i in range(101):
                time = intervalTime * i
                voltage = B * (1 - exp((-time)/(R * C)))
                result = '%7.0f: %14.5f\n' %(time, voltage)
                outFile.write(result)

        except IOError:
            print('Cannot write file!')
        finally:
            outFile.close()

    except IndexError:
        print('Wrong format!')
    except TypeError:
        print('Wrong format!')




except IOError:
    print('Wrong file!')




