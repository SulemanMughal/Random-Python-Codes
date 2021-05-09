def print_menu(header, *special, **items):
    print(header)

    print("-----Specials of Today-----")
    for name in special:
        print(name)

    print("--All Items--")
    for name in items.keys():
        print(name, ":", items[name])


print_menu("--Menu--", "Fish", "chicken", steak = "49 USD", salad = "19 USD", soup = "10 USD")
