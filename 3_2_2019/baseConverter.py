def baseConverter(number, base):
    new= 0
    i=0
    while(number >0):
        new = new+(number%base)*(10**i)
        number //= base
        i +=1
    print(new)
