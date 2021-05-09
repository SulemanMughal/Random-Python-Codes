myString = input('Enter a String: ')
try:
    print('Cancatenating String and Integer')
    print('String # ' + 1 + " : " + myString)
    myInt = int(myString)
    print(myInt)
except ValueError as error:
    print(error)

except TypeError as error:
    print(error)

