#Problem No.19

#Three sides of the triangle
print("Enter the length of the Three sids of a Triangle")
x =  float(input("Base: "))
y = float(input("Perpendicular: "))
z = float(input("Hypotenuse : "))

if (z**2) == ( (x**2) + (y**2)):
    print("Right Triangle")
elif x == y and y == z:
    print("Equilateral Triangle")
elif (x == y or y == z or z == x):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

