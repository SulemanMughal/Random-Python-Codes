#Problem No.16

print("Enter the values of diffrent angles of a triangle")
alpha = float(input("Alpha: "))
beta = float(input("Beta: "))
gamma = float(input("Gamma: "))
if int((alpha + beta + gamma)) == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
