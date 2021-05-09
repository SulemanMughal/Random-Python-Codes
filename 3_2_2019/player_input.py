def player_input():
    marker = ''
    A = ['X', 'x', 'O', 'o']
    while marker not in A:
        marker = input("Player 1 choose X or O : ")

    if 'X' == marker.upper():
        return ('x', 'o')
    else:
        return ('o', 'x')
