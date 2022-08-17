"""
Tic Tac Toe Player
"""

import math
from multiprocessing.sharedctypes import Value
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x +=1
            if board[i][j] == O:
                y +=1
    if y < x:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append([i,j])
    if len(actions): 
        return actions
    else:
        return 0


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    
    if newboard[action[0]][action[1]] == EMPTY:
        newboard[action[0]][action[1]] = player(board)
        return newboard
    else:
        raise Exception("invalid move")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for i in range(3):
        if board[i] == [O,O,O]:
            return O
        if board[i] == [X,X,X]:
            return X
    #check columns
    for i in range(3):
        columns = []
        #cycling through slot i of each row, resetting columns[]
        for j in range(3):
            if board[j][i] == X:
                columns.append(X)
            if board[j][i] == O:
                columns.append(O)
        if columns == [O,O,O]:
            return O
        if columns == [X,X,X]:
            return X
    # check diagonals
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    if diagonal1 == [X,X,X] or diagonal2 ==[X,X,X]:
        return X
    if diagonal1 == [O,O,O] or diagonal2==[O,O,O]:
        return O
    return None
                

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # maximizing player picks action in actions that produce highest value of utility
    # maxi = X, mini = O
    if terminal(board):
        return None
    moves= []
    if player(board) == X:
        # try to maximize points
        for move in actions(board):
            moves.append((minvalue(result(board, move)), move))
        moves = sorted(moves, key=lambda moves:moves[0], reverse = True)
        return moves[0][1]
    else:
        # try to minimize points
        for move in actions(board):
            moves.append((maxvalue(result(board, move)), move))
        moves = sorted(moves, key=lambda moves:moves[0])
        return moves[0][1]

def maxvalue(board):
    """
    returns the points of the move that produces the highest value result
    """
    points = -1000
    if terminal(board):
        return utility(board)
    for move in actions(board):
        points = max(points, minvalue(result(board, move)))
    return points

def minvalue(board):
    """
    returns the points of the move that produces the lowest value result
    """
    points = 1000
    if terminal(board):
        return utility(board)
    for move in actions(board):
        points = min(points, maxvalue(result(board, move)))
    return points