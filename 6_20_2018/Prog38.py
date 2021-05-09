read = open('Hello.txt', 'r')

for line in read:
    print(line.rstrip())

read.close()

print('File closed : ', read.closed)

