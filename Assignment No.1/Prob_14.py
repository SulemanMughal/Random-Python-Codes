#Problem No.14
print("Enter Three Different Integer: ", end = '\t')
num1 = int(input())
num2 = int(input())
num3 = int(input())

print("Sum is " ,(num1 + num2 + num3))
print("Average is ", (num1 + num2 + num3)/3)
print("Product is ", (num1 * num2 * num3))
print("Smallest is ", min(num1, min(num2, num3)))
print("Largest is ", max(num1,max(num2, num3)))

def max(x,y):
    if x > y:
        return x
    else:
        return y

def min(x,y):
      if x < y :
          return x
      else:
          return y
