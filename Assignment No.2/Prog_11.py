#Problem No.11

import random

def flip():
    return (round(random.random()))


i = 1
Head  = 0
Tail = 0
while i <= 100:
    if flip() == 0:
        print("Head")
        Head += 1
    else:
        print("Tail")
        Tail += 1
    i += 1

print("Heads: ", Head)
print("Tails: ", Tail)


