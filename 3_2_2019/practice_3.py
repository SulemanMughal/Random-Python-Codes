#Python Zip Function


A = [1, 2, 3]

B = ['a', 'b', 'c']

for item in zip(A, B):
    print(item)
    
C = ['Suleman', 'Shahid', 'Mehmood', 'Mughal']

for i in zip(A, B, C):
    print(i)
    
A = [1, 2, 3, 4, 5, 6]

print(list(zip(A, B, C)))
