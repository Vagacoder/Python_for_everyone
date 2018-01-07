## Ch08 P8.5

def main():
    studentScore = {}
    
    printMenu()
    choice = input('Please enter your choice: ').lower()
    print(choice)
    while choice != 'q':
        if choice == 'a':
            addStudent(studentScore)
        elif choice == 'r':
            removeStudent(studentScore)
        elif choice == 'm':
            modifyGrades(studentScore)
        elif choice == 'p':
            printAll(studentScore)
        elif choice == 'q':
            break
        else:
            print('Wrong input, please try again.\n')
                         
        printMenu()
        choice = input('Please enter your choice: ').lower()
    
    print('Thanks for using system!')

        
def printMenu():
    print('A: add student')
    print('R: remove student')
    print('M: modify grades')
    print('P: print all grades')
    print('Q: quit')

def addStudent(inputDict):
    name = input('Please enter the name of student: ')
    grade = input('Please enter the grade of student: ') 
    if name in inputDict:
        print('Student already recorded, please use \'Modify grades\'.')
        return
    else:
        inputDict[name] = grade
        print('Student and his grade are added successfully!\n')
    
    
def removeStudent(inputDict):
    name = input('Please enter the name of student: ')
    if name not in inputDict:
        print('Student not found.\n')
        return
    else:
        confirm = input('Are you sure to remove this student? (Y/N): ').lower()
        if confirm == 'y':
            inputDict.pop(name)
            print('Student and his grade are removed successfully!\n')
        else:
            print('Operation cancled.\n')
            return
    
    
def modifyGrades(inputDict):
    name = input('Please enter the name of student: ')
    grade = input('Please enter the grade of student: ') 
    if name not in inputDict:
        print('Student is not recorded, please use \'Add student\'.\n')
        return
    else:
        inputDict[name] = grade
        print('Student and his grade are modified successfully!\n')
    

def printAll(inputDict):
    if len(inputDict) == 0:
        print('There is no record.\n')

    else:
        for stu in sorted(inputDict):
            print(stu +':', inputDict[stu])
        print()
        
        

main()