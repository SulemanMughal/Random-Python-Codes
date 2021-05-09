#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.

n = int(input('Ener number to clculate factorial : '))

product = 1
for i in range(1, n+1):
    product *= i


print(product)
