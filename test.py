import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, X, O],
            [EMPTY, X, O],
            [EMPTY, EMPTY, X]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turns = 0
    for row in board:
        for i in range(len(row)):
            if row[i] != None:
                turns += 1
    if turns % 2 == 0:
        print(f"{X} - Player Function")
        return X
    else:
        print(f"{O} - Player Function")
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i, row in enumerate(board):
        for j in range(len(row)):
            if row[j] == None:
                actions.append((i,j))
    print(f"{actions} - Actions Function")
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    if board[action[0]][action[1]] == None:
        newBoard[action[0]][action[1]] = player(board)
        print(f"{newBoard} - Result Function")
        return newBoard
    else:
        raise Exception("This Action Can't be taken")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != None:
            print(f"{board[i][0]} - Winner Function")
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != None:
            print(f"{board[0][i]} - Winner Function")
            return board[0][i]
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] or board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != None:
            print(f"{board[1][1]} - Winner Function")
            return board[1][1]
        
    print("None - Winner Function")
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) == None:
        for row in board:
            for i in range(len(row)):
                if row[i] == None:
                    print(f"False - Terminal Function")
                    return False
    print(f"True - Terminal Function")
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        print(f"{1} - Utility Function")
        return 1
    elif winner(board) == O:
        print(f"{-1} - Utility Function")
        return -1
    else:
        print(f"{0} - Utility Function")
        return 0
    


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        print("Returning None - Minimax")
        return None
    else:
        if player(board) == X:
            v = -math.inf
            for action in actions(board):
                k = min_value(result(board, action))
                if k > v:
                    v = k
                    best_move = action
        else:
            v = math.inf
            for action in actions(board):
                k = max_value(result(board, action))
                if k < v:
                    v = k
                    best_move = action
        print(best_move)
        return best_move


# player(initial_state())
# actions = actions(initial_state())
# result(initial_state(), actions[0])
# winner(initial_state())
# terminal(initial_state())
# utility(initial_state())
minimax(initial_state())
