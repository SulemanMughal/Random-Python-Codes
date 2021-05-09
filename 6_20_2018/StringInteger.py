myString = input('Enter a String: ')
try:
    print('Converting String to Integer')
    myInt = int(myString)
    print(myInt)
except:
    print('Can\'t Convert! String is non-numeric')

print("DONE!")
