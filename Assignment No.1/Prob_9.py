#Problem No.9

Gender = input("Male/Female[M/F] : ")
Married = input("Are you married?[Y/N] : ")
Age = int(input("Enter Your Age: "))

if Gender == 'Male':
    if Married == 'No' and Age >= 30:
        print("The Driver is to be Insured.")
elif Married == 'No' and Age >= 25:
        print("The Driver is to be Insured.")
else :
    print("The Driver is not to be Insured.")
    
