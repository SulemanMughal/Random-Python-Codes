import numpy
n = numpy.arange(18)
print(type(n))
print(n)
n = n.reshape(3,3,2)
print("After Rehape")
print(n)
n = [1,2,3,4,5]
n = numpy.asarray(n)
print("Convert the input to an array")
print(n)
