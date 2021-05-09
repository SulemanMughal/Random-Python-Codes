read = open('textfile.txt', 'w')

read.write('Python is a great language\n')
read.write('Yeah its great!\n')

read.close()

print("File Closed : ", read.closed)

