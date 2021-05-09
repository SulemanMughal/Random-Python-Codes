quote = "Do small things with great love"
print(quote)

print(quote.find('small things'))

print(quote.find("small things", 10))

print(quote.find("small things", 2))

print(quote.find("o small ",10, -1))

print(quote.find("things ", 6, 20))

quote = "let it be, let it be, let it be"

print(quote)

result = quote.find("let it be")
print(result)

print(quote.find("samll"))

if quote.find("be") != -1:
    print("Containing")
else:
    print("Doesn't Containing.")
    
