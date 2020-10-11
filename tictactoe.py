"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

class IvalidActionError(Exception):
    def __init__(self,expression):
        self.expression = expression

def initial_state():
    """
    Returns starting state of the board.
    """
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    return board

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j]) == X:
                xcount += 1
            if (board[i][j]) == O:
                ocount += 1
    if xcount == 0 and ocount == 0:
        return X
    if xcount == ocount:
        return X
    if (xcount - ocount) == 1:
        return O

    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                dvojka = (i,j)
                s.append(dvojka)
    return s
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #if type(board) != list or type(action) != int:
        #(type(board),type(action))
    if board[action[0]][action[1]] != EMPTY:
        raise IvalidActionError("exception")

    kopie = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if i == action[0] and j == action[1]:
                kopie[i][j] = player(board)
    return kopie

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for num in range(3):
        if board[num][0] == board[num][1] and board[num][1] == board[num][2]:
            print(board)
            print(board[num][0])
            return board[num][0]
        if board[0][num] == board[1][num] and board[1][num] == board[2][num]:
            print(board)
            print(board[0][num])
            return board[0][num]
        if board[1][1] == (board[0][0] and board[2][2]) or board[1][1] == (board[0][2] and board[2][0]):
            print(board)
            return board[1][1]
        else:
            return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    fcount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X or board[i][j] == O:
                fcount +=1 
    print(winner(board))
    if (fcount == 9 or ((winner(board) == X or (winner(board) == O)))):
        return True
    else:
        return False

    raise NotImplementedError




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError
 

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = -1
            v = max(v, minimax(result(board, action)))
            return v

    if player(board) == O:
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = 1
            v = min(v, minimax(result(board, action)))
            return v
    