myString = input('Enter a String : ')
print('Converting String to Integer')
if myString.isdigit() == True:
    myInt = int(myString)
    print(myInt)
else:
    print('String is non-numeric')
print('DONE!')
