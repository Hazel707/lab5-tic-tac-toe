# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    winner=None
    for row in range(0,3):
        if (board[row][0]==board[row][1]==board[row][2]):
            winner= board[row][0]
        if winner !=None:
            break
    for col in range(0,3):
        if (board[0][col]==board[1][col]==board[2][col]):
            winner=board[0][col]
        if winner !=None:
            break

    if board[0][0] == board[1][1] == board[2][2]:
        winner=board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        winner=board[0][2]
    return winner

def isfull(board):
    full=True #Ture=grid is full
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col]==None:
                full=False
                break
    return full

def check_move(board,row,col):
    if board[row][col]!=None:
        return True
    else:
        return False

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player=="X":
        return "O"
    else:
        return "X"
    #return "O"  # FIXME

def make_move(board,player1,player2,now,row,col):
    if now==1:
        board[row][col]=player1
    else:
        board[row][col]=player2
    return board

    