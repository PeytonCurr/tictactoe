import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[O, X, X],
            [O, X, EMPTY],
            [O, EMPTY, EMPTY]]


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
        print(X)
        return X
    else:
        print(O)
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
    print(actions)
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    if board[action[0]][action[1]] == None:
        newBoard[action[0]][action[1]] = player(board)
        print(newBoard)
        return newBoard
    else:
        raise Exception("This Action Can't be taken")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != None:
            print(board[i][0])
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != None:
            print(board[0][i])
            return board[0][i]
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] or board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != None:
            print(board[1][1])
            return board[1][1]
        
    print("None")
    return None



player(initial_state())
actions = actions(initial_state())
result(initial_state(), actions[0])
winner(initial_state())
