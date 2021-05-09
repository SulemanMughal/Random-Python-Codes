myString = "1"
try:
    print('Converting myString to int')
    myInt = int(myString)
    print(myInt)
except (ValueError, TypeError) as error:
    print(error)
except Exception as error:
    print(error)
else:
    print('No error occured')
