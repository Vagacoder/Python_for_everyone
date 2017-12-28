## Ch07 P7.30

try:
    inFile = open('hotelservice.txt', 'r')
    line = inFile.readline()
    serviceList = []
    amountList = []

    while line != '':

        try:
            data = line.split(';')
            name = data[0].strip()
            service = data[1].strip()
            amount = float(data[2].strip())
            date = data[3].strip()

            if service in serviceList:
                index = serviceList.index(service)
                amountList[index].append(amount)
            else:
                serviceList.append(service)
                amountItem = [amount]
                amountList.append(amountItem)

        except IndexError:
            print('Some data is not in correct format! Index')

        except TypeError:
            print('Some data is not in correct format! Type')

        except ValueError:
            print('Some data is not in correct format! Value')

        line = inFile.readline()

    inFile.close()
    print(serviceList)
    print(amountList)

    for i in range(len(serviceList)):
        service = serviceList[i]
        outFile = open(service + '.txt', 'w')
        outFile.write(service + ':\n')
        for item in amountList[i]:
            outFile.write(str(item) + '\n')
        outFile.close()

except IOError:
    print('File does not exist!')

