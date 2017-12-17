## Ch03 P3.8

#num1 = int(input('Please enter first number: '))
#num2 = int(input('Please enter second number: '))
#num3 = int(input('Please enter third number: '))
#num4 = int(input('Please enter forth number: '))

num1 = 1
num2 = 2
num3 = 3
num4 =4

if (num1 == num3 and num2 == num4) or (num1 == num4 and num2 == num3):
    print('two pairs')

else:
    print('not two pairs')

## Ch03 P3.12

grade = input('Please enter the letter grade: ').upper()

score_plus = 0.0

if len(grade) == 2:
    if grade[1] == '+' and grade[0] != 'A' and grade[0] != 'F':
        score_plus = 0.3

    elif grade[1] == '-' and grade[0] != 'F':
        score_plus = -0.3

if grade[0] == 'A':
    score = 4

elif grade[0] == 'B':
    score = 3
elif grade[0] == 'C':
    score = 2
elif grade[0] == 'D':
    score = 1
elif grade[0] == 'F':
    score =0


print('The numeric value is %.1f' %(score + score_plus))
