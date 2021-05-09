from space_check import space_check

def player_choice(board):
    position = 0
    while position not in list(range(1, 10)) and ( space_check(board, position)):
        position = int(input('Choose a position (1 - 9) : '))

    return position
