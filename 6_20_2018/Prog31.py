read = open('textfile.txt', 'w')

read.write('This is a test\n')
read.write('To add more lines.\n')

read.close()

print('File closed:', read.closed)

