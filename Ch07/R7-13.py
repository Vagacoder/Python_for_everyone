##Ch07 R7.13

def getISO8601Date(year, month, day, hour, minute):
    year = str(year)

    if month <10:
        month = "0" + str(month)
    else:
        month = str(month)

    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    ISO8601Date = year + "-" + month + "-"+day + " " + hour +":" + minute

    return ISO8601Date

def main():

    print(getISO8601Date(2011, 3, 1, 9, 35))

main()