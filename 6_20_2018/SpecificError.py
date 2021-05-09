myString = input('Enter a string : ')
try:
    print('Converting String to integer: ')
    myInt = int(myString)
    print(myInt)
except ValueError:
    print('Can\'t convert. String is non-numeric')

print('DONE!')
