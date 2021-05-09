#Dictionary Explanation ...
A = {'Name': 'Suleman Shahid', 'Age' : 22}
print(A)

print(A['Name'])
print(A['Age'])

print(len(A))

#Update Dictionary Variable ...

A['Age'] = 23
print(A)
A['Address'] = "Lahore, Pakistan"
print(A)

#Removing Dictionary Elements ...
del A['Address']
print(A)

#Remove All dictionary Elements...
A.clear()

print(A)

#Delete Entire Dictionary
del A

#print(A)
