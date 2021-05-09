read = open('textfile.txt', 'r')

for line in read:
    print(line, end ='')

read.close()

