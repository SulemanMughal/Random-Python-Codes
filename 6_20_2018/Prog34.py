with open('HelloWorld.txt') as file:
    count = 0
    for line in file:
        words = line.split()
        print(words)
        count += len(words)

    print('Total Number of characters in File: ', count)
        







