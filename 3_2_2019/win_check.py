def win_check(board, mark):
    if (board[1] == mark and board[4] == mark and board[7] == mark):
        return True
    elif (board[2] == mark and board[5] == mark and board[8] == mark):
        return True
    elif (board[3] == mark and board[6] == mark and board[9] == mark):
        return True
    elif (board[7] == mark and board[8] == mark and board[9] == mark):
        return True
    elif (board[4] == mark and board[5] == mark and board[6] == mark):
        return True
    elif (board[1] == mark and board[2] == mark and board[3] == mark):
        return True
    elif (board[1] == mark and board[5] == mark and board[9] == mark):
        return True
    elif (board[7] == mark and board[5] == mark and board[3] == mark):
        return True
    else:
        return False
