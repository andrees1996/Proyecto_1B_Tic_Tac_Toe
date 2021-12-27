"""
Tic Tac Toe Player
"""

import math

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

    """si es el primer movimiento entonces , se establece x como primer movimiento y en este caso se compara con la funcion initial_state()"""
    numero_piezas_X = 0
    numero_piezas_O = 0
    if board == initial_state():
        return X

    for fila in board:
        """por cada fila se contra el numero de X e O que se encuentran en el tablero para de esta manera poder determinar el movmiento"""
        numero_piezas_X = numero_piezas_X + fila.count(X);
        numero_piezas_O = numero_piezas_O + fila.count(O)

    if numero_piezas_X > numero_piezas_O
        return O
    if numero_piezas_O == numero_piezas_X
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
