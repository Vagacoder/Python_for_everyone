## Ch08 R8.8 R8.9 R8.10

months = {1:'January', 2:'Febuary', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 
          10:'October', 11:'November', 12:'December'}

print(months[1])


months1 = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 
          'October', 'November', 'December']

print(months1.index('November')+1)

dict1 = {'Jan':'','Feb':'', 'Mar':'', 'Apr':''}
dict2 = {'Jan':'', 'May':'', 'Mar':'', 'Jun':''}

list1 = []
for key in dict1:
    if key in dict2:
        list1.append(key)

print(list1)