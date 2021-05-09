A = ['A', 'B' , 'C']
B = [1,2,3]
print(A, B)
for i, j in zip(A, B):
    print('{0} : {1}'.format(i, j))
