#Problem No.9

def Fahrenheit2Celsius(num):
    celsius = (num-32)*(5/9)
    return celsius

def Celsius2Fahrenheit(num):
    fahrenheit = num* (9/5) + 32
    return fahrenheit


def printChart():
    i = 0
    print("Celsius\t|\tFahrenheit")
    while i <= 100:
        print(i,"\t|\t", round(Celsius2Fahrenheit(i), 2), sep = '')
        i += 1

    i = 32
    print("Fahrenheit\t|\tCelsius")
    while i<= 212:
        print(i, "\t|\t", round(Fahrenheit2Celsius(i), 2), sep = '')
        i += 1
