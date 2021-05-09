def greet(*names):
    for name in names:
        print("Hello", name)

A = ('Suleman', 'Shahid', 'Mehmood', 'Mughal')
greet(*A)


greet("UET", "Lahore", "Campus")
