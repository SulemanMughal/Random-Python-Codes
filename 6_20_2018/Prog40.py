with open('Hello.txt') as read:
    lines = read.readlines()

for line in lines:
    print(line.rstrip())

print(lines)


for i in lines:
    print(i)
