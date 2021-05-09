#Problem No.3

print("Enter Your Marks in the following subjects")
Sub_1 = float(input("ITC                :   "))
Sub_2 = float(input("Calculus           :   "))
Sub_3 = float(input("Physics            :   "))
Sub_4 = float(input("Thermodynamics     :   "))
Sub_5 = float(input("Circuit-1          :   "))

print("Percentage Marks in each subject")
print("ITC              :", (Sub_1/100*100), "%")
print("Calculus         :", (Sub_2/100*100), "%")
print("Physics          :", (Sub_3/100*100), "%")
print("Thermodynamics   :", (Sub_4/100*100), "%")
print("Circuit-1        :", (Sub_5/100*100), "%")

sum = (Sub_1 + Sub_2 + Sub_3 + Sub_4 + Sub_5)
print("Total marks obtained     : ", sum)
print("The overall percentage   : ", (sum/500)*100 , "%")
