#Problem No.27

hours = int(input("Enter No. of Hours worked(-1 to end): "))
rate = int(input("Enter hourly rate of the worker($00.00): "))

while hours != -1 :
    print("Salary is $", (hours * rate), sep='')
    hours = int(input("Enter No. of Hours worked(-1 to end): "))
    if hours == -1:
        break
    rate = int(input("Enter hourly rate of the worker($00.00): "))

