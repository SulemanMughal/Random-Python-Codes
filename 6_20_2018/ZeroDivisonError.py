dividend = int(input('Enter Dividend : '))
divisor = int(input('Enter Divisor : '))
try:
    result = dividend/divisor
    print('Result : ', result)
except ValueError as error:
    print(error)
