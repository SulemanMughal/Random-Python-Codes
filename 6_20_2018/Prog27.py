read = open('textfile.txt', 'r+')

str = read.read()

print(str)

read.close()

print('File Closed: ' , read.closed)
