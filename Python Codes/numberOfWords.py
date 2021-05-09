#Count Number of words...
A = ["Suleman Shahid Mehmood Mughal",
     "University of Engineering anf Technology",
     "Lahore, Punjab, Pakistan",
     "Department of Electrical Engineering"]

print(A)

words = 0
for i in A:
    for j in i:
        if j == " ":
            words += 1
    words += 1
print("Total Number of Words : " , words)
