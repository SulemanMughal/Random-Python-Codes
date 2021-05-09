#Problem No. 15

weightInKilograms = float(input("Enter Weight (Kilograms): "))
heightInMeters = float(input("Enter Height (Meters): "))

BMI = weightInKilograms/(heightInMeters**2)

print("Your Body Mass Index (BMI) is ", BMI)

print("BMI VALUES")
print("Underweight: less than 18.5")
print("Normal: between 18.5 and 24.9")
print("Overweight: between 25 and 29.9")
print("Obese: 30 or greater")
