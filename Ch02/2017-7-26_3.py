## Ch02 P2.17 Time calculation. KEY: convert all time data to minutes

MIN_PER_HOUR = 60

firstTime = int(input('Please enter the first time: '))
secondTime = int(input('Please enter the second time: '))

firstT_minute = firstTime//100*MIN_PER_HOUR + firstTime%100       #convert time date to minutes
secondT_minute = secondTime//100*MIN_PER_HOUR + secondTime%100

timeDifference = (secondT_minute - firstT_minute)+24*MIN_PER_HOUR  # in case 2nd time is on second day

hour = timeDifference//60%24             # %24 for the case that 2nd time is smaller than 1st time
minute = timeDifference%60

print(hour, 'hours', minute, 'minutes')


