import math
def nthRootLog(x, n):
    result = pow(10, ((1/n)*math.log10(x)))
    print(result)

nthRootLog(34,6)
