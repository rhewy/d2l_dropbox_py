from ..StudentInfo import StudentInfo 
test1 = StudentInfo()
print(test1.firstName)
print(test1.lastName)
print(test1.bcitID)

test2 = StudentInfo('Robert', 'Hewlett', 'A00000002')
print(test2.firstName)
print(test2.lastName)
print(test2.bcitID)

test3 = StudentInfo('Robert', 'Hewlett', 'A00000002')

if(test2 == test3):
    print('Same')
else:
    print('Different')

studentList = [test2]

if test3 in studentList:
    print('In the list')
else:
    print('NOT in the list')

if test1 in studentList:
    print('In the list')
else:
    print('NOT in the list')