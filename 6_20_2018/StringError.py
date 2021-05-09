myString = input('Enter a string: ')
try:
    print('Converting String to Integer')
    myInt = int(myString)
    print(myInt)
except ValueError as error:
    print(error)
