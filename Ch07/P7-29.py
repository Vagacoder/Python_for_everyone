## Ch07 P7.29

try:
    inFile = open('hotelservice.txt', 'r')
    line = inFile.readline()
    serviceList = []
    totalAmountList = []

    while line != '':

        try:
            data = line.split(';')
            name = data[0].strip()
            service = data[1].strip()
            amount = float(data[2].strip())
            date = data[3].strip()

            if service in serviceList:
                index = serviceList.index(service)
                totalAmountList[index] += amount
            else:
                serviceList.append(service)
                totalAmountList.append(amount)

        except IndexError:
            print('Some data is not in correct format! Index')

        except TypeError:
            print('Some data is not in correct format! Type')

        except ValueError:
            print('Some data is not in correct format! Value')

        line = inFile.readline()

    inFile.close()
    print(serviceList)
    print(totalAmountList)

except IOError:
    print('File does not exist!')

