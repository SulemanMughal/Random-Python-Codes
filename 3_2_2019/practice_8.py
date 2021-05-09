from random import randint


celcius = [randint(0,100) for x in range(11)]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]


print(celcius)
print(fahrenheit)


