myString=  input('Enter a string: ')
try:
    print(1/0)
    print('Concatenating String and Integer')
    print('String # ' + "1 " + + ": " + myString)
    myInt = int('12')
    print(myInt)
except (ValueError, TypeError):
    print(error)

except Exception:
    print('Some other kind of error')
