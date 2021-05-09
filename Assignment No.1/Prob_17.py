#Problem No.17

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length*breadth
perimeter = 2 * (length+breadth)

if area > perimeter:
    print("Area = ", area , " is greater than its periemeter = ", perimeter)
elif area == perimeter:
    print("Area = " , area , " is equal to its perimeter = ", perimeter)
else:
    print("Area = ", area , " is less than its perimeter = ", periemter)
