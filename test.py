import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[O, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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


player(initial_state())
actions = actions(initial_state())
result(initial_state(), actions[0])
