"""
Tic Tac Toe Player
"""
import math
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

    """si es el primer movimiento entonces , se establece x como primer movimiento y en este caso se compara con la funcion initial_state()"""
    numero_piezas_X = 0
    numero_piezas_O = 0
    if board == initial_state():
        return X

    for fila in board:
        """por cada fila se contra el numero de X e O que se encuentran en el tablero para de esta manera poder determinar el movmiento"""
        numero_piezas_X = numero_piezas_X + fila.count(X)
        numero_piezas_O = numero_piezas_O + fila.count(O)

    if numero_piezas_X > numero_piezas_O:
        return O
    elif numero_piezas_O == numero_piezas_X:
        return X

def actions(board):
    """Se debe devolver n conjunto de todas las acciones posibles que se pueden tomar en el tablero"""
    conjunto_movimientos = []
    """como se debe devolver una tupla, se tiene que realizar una matri bidimensional y recorrer en ella """
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] == EMPTY:
                conjunto_movimientos.append([fila, columna])
    return conjunto_movimientos

def result(board, action):
    """se realiza la copia del trablero"""
    copia_board = copy.deepcopy(board)

    if copia_board[action[0]][action[1]] != EMPTY:
            raise IndexError
    else:
        copia_board[action[0]][action[1]] = player(copia_board)
        return copia_board


def winner(board):
    columns = []
    """aqui se verifica si es que existio un ganador , a traves de las filas de la tabla"""
    for fila in board:
        numero_piezas_X = fila.count(X)
        numero_piezas_O = fila.count(O)
        if numero_piezas_X == 3:
            return X
        if numero_piezas_O == 3:
            return O

    """aqui se verifica si es que existio un ganador , a traves de las columnas de la tabla"""
    for columna in range(len(board)):
        column = [fila[columna] for fila in board]
        columns.append(column)
    """si el numero de piezas X e O es igual a tres en cualquiera de las columnas se retorna X u O"""
    for columna in columns:
        numero_piezas_X = columna.count(X)
        numero_piezas_O = columna.count(O)
        if numero_piezas_X == 3:
            return X
        if numero_piezas_O == 3:
            return O

    """se verifica si es que existio un ganador a trves de las diagonales de la tabla"""

    """Se verifica si existio el ganador O a traves de las diagonales"""
    if (board[1][1] == O and board[0][0] == O and board[2][2] == O) or (board[1][1] == O and board[0][2] == O and board[2][0] == O):
        return 0
    """Se verifica si existio el ganador X a traves de las diagonales"""
    if (board[1][1] == X and board[0][0] == X and board[2][2] == X) or (board[1][1] == X and board[0][2] == X and board[2][0] == X):
            return X

    """Si existe empate"""
    return None


def terminal(board):
    """verifica si el juego a terminado"""
    contador = 0
    for fila in board:
        """cuenta las celdas que estan vacias"""
        contador = contador + fila.count(EMPTY)
        """si el contador tiene como valor final 0 , quiere decir que se completaron todas las celdas"""
    if contador == 0:
        return True
        """se llama al metodo winner para determinar si existio un ganador"""
    elif winner(board) is not None:
        return True
        """si no paso ninguna de las dos opciones, quiere decir que aun existen casillas vacias"""
    else:
        return False


def utility(board):
    """si el ganador es X retorna 1, si el ganador es o retorna -1 y si existe un empate retorna 0"""
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    jugador = player(board)

    if jugador == X:
        v = -math.inf
        for movimiento in actions(board):
            k = min_value(result(board, movimiento))  # FIXED
            if k > v:
                v = k
                best_move = movimiento
    else:
        v = math.inf
        for movimiento in actions(board):
            k = max_value(result(board, movimiento))  # FIXED
            if k < v:
                v = k
                best_move = movimiento
    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for movimiento in actions(board):
        v = max(v, min_value(result(board, movimiento)))
    return v    #FIXED

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for movimiento in actions(board):
        v = min(v, max_value(result(board, movimiento)))
    return v    #FIXED
