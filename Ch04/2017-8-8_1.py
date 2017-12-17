## Ch04 P4.3 and P4.10

#string = input('Please enter a string: ')
string = 'We are Students of SBCC'

for i in string:
    if i.isupper():
        print(i, end=' ')

print()
position = 0

while position < len(string):
    if position %2 == 0:
        print(string[position], end=' ')
    position +=1

print()
position = 0
new_s =''
while position < len(string):
    if string[position].lower() in 'aeiou':
        new_s += '_'
    else:
        new_s += string[position]

    position +=1

print(new_s)

print()
position = 0
vowel_num = 0
while position < len(string):
    if string[position].lower() in 'aeiouy':
        print(string[position],': ',position +1)
        vowel_num += 1

    position +=1

print ('Vowel number is:',vowel_num)