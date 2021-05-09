read = open('textfile.txt', 'r')


str = read.readlines()
print(str[::-1])

read.close()

print('File closed: ', read.closed)

