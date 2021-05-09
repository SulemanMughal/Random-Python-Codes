foo =  open('Hello.txt','r')

print(foo.mode)
print("File Name: ", foo.name)

print("File Open: ", str(foo.close))

foo.close()
