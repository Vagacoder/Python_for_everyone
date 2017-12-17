## P4.33

card_num = input('Please enter card number (8 digits): ')
while len(card_num) != 8:
    print('Wrong number.')
    card_num = input('Please enter card number (8 digits): ')


string1 = int(card_num[7]) + int(card_num[5]) + int(card_num[3]) + int(card_num[1])
#print(string1)

string2 = str(int(card_num[6])*2) + str(int(card_num[4])*2) + str(int(card_num[2])*2) + str(int(card_num[0])*2)
#print(string2)
string2_1 =0

for i in string2:
    string2_1 += int(i)

#print(string2_1)

string3 = string1 + string2_1

if string3%10 == 0:
    print('This is a valid number.')
else:
    print('This is NOT a valid number.')

    correct_last_in_string1 = 10 - (string2_1 % 10)
    other_in_string1 = int(card_num[5]) + int(card_num[3]) + int(card_num[1])
    last_of_other_in_string1 = other_in_string1%10
    if correct_last_in_string1 > last_of_other_in_string1:
        correct_last_in_card = correct_last_in_string1 - last_of_other_in_string1
    elif correct_last_in_string1 < last_of_other_in_string1:
        correct_last_in_card = correct_last_in_string1 + 10 - last_of_other_in_string1

    print('The correct last digit on card should be %d: '%correct_last_in_card)

