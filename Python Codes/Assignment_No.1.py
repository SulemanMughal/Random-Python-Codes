string = "Univsersity of Engineering and Technology"
i = 0
listA = []
for i in range(len(string)):
    if string[i] == 'a' or  string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
        listA.append(string[i])

print("Reverse Vowels List")
i = 0
print("[", end = " ")
for i in range(len(listA)):
    print(listA[len(listA)-i-1], end = " ")

print("]")
print("Total Number of Vowels in the given string: ", len(listA))
