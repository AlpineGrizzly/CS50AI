"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
rows = 3
cols = 3

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
    num_x = 0
    num_o = 0
    
    # Count the X's and O's
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == X:
                num_x += 1
            elif board[i][j] == O:
                num_o += 1

    # If we have equal moves, it's X turn again
    if num_x == num_o:
        return "X"
    return "O"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moveset = []
    
    # If the move is available, add it to the set
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == EMPTY:
                moveset.append((i, j))

    return moveset


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    res_board = board
    print("action is ", action)
    res_board[action[0]][action[1]] = player(board)
    return res_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check win conditions 
    ## Horizontal
    for i in range(rows):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O

    ## Vertical  
    for i in range(cols):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O

    ## Diagonal 
    if board[1][1] == X and ((board[0][0] == board[2][2] == X) or (board[0][2] == board[2][0] == X)):
        return X 
    if board[1][1] == O and ((board[0][0] == board[2][2] == O) or (board[0][2] == board[2][0] == O)):
        return O 

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if either player has won
    if winner(board) is not None:
        return True

    # If board is filled
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == EMPTY:
                return False
        
    return True # If we get past all the cases, the game is over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O: 
        return -1
    return 0

def maxvalue(board):
    """
    Returns an action on the board that produces the smallest value for max player
    """
    newboard = board
    best_score = -math.inf
    curr_score = best_score
    best_action = (None, None)  # Holds highest min action as of far
    
    for a in actions(board):
        minv, _ = minvalue(result(newboard, a))
        curr_score = max(curr_score, minv)       
        if curr_score > best_score or best_action is None:
            best_action = a
            best_score = curr_score
    return best_score, (best_action)

def minvalue(board):
    """
    Returns an action on the board that produces the highest value for min player 
    """
    newboard = board
    best_score = math.inf 
    curr_score = best_score
    best_action = (None, None) # Holds highest min action as of far

    for a in actions(board):
        maxv, _ = maxvalue(result(newboard, a))
        curr_score = min(curr_score, maxv)
        if curr_score < best_score or best_action is None:
            best_action = a
            best_score = curr_score
    return best_score, (best_action)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    maxturn = False
    action = (None, None) # Optimal action for current player

    if player(board) == X:
        maxturn = True # X will be the Max player, while O is the min player
    
    # Calculate Max and Min values 
    ## Base case: Terminal state no moves to be made
    if terminal(board):
        return utility(board)

    # Run Max or min function on board for action based on whos turn it is 
    #score, action = minvalue(board) if maxturn else maxvalue(board)
    action = actions(board)[0]
    
    return action
    
    


