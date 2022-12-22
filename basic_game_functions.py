import numpy as np
import os
from scipy.ndimage import convolve


def create_gameboard(input_array = None, rows = None, cols = None, origin=(0,0)):
    if input_array is None:
        input_array = np.full((rows,cols), False)
    return (input_array, origin)


def get_neighbour_indices(row: int, col: int, rows: int, cols: int) -> list[int]:
    toprow = (row - 1) % rows
    bottomrow = (row + 1) % rows
    leftcol = (col-1) % cols
    rightcol = (col+1) % cols
    res = [toprow, bottomrow, leftcol, rightcol]
    return res


def print_gameboard(gameboard : np.array):
    """Gibt das Gameboard in die Konsole aus, wie in OneNote definiert.

    Args:
        gameboard (np.array): Das Gameboard, also eine nxn Numpy Matrix mit bool
    """
    txt = get_gameboard_text(gameboard)
    print(txt)

def get_gameboard_text(gameboard, horizontal_separator : bool = True) -> str:
    """Generiert einen text string von einem Gameboard

    Args:
        gameboard: Das Gameboard, also eine nxn Numpy Matrix mit bool
    """
    rows = gameboard[0].shape[0]
    cols = gameboard[0].shape[1]
    
    
    sep_line = ' ---' * cols + ' '
    
    if horizontal_separator:
        res = sep_line +  os.linesep
    else:
        res = ''

    for row in range(rows):
        
        second_line = '|'
        for col in range(cols):
            # Zelle:
            # 1. Zelle in gameboard abfragen
            cell_value = gameboard[0][row, col]
            # 2. wenn false, dann '   |'
            if cell_value == False:
                cell_string = '   |'
            # 3. sonst: ' o |'
            else:
                cell_string = ' o |'
            # 4. Zelle zu second_line hinzufügen
            second_line += cell_string
        # second_line ausgeben
        
        res = res + second_line + os.linesep
        if horizontal_separator:
            res = res + sep_line + os.linesep

    
    res = res[:-1]
    
    return res


def get_gameboard_text_compact(gameboard : np.array) -> str:
    """Generiert einen text string von einem Gameboard, z.B. zur Ansicht mit Webdings font

    Args:
        gameboard (np.array): Das Gameboard, also eine nxn Numpy Matrix mit bool
    """

    # NOTE: das funktioniert, weil der Webdings font Symbole anstatt normale Buchstaben anzeigt.

    rows = gameboard[0].shape[0]
    cols = gameboard[0].shape[1]
    
    res = ''

    for row in range(rows):
        second_line = ''
        for col in range(cols):
            # Zelle:
            # 1. Zelle in gameboard abfragen
            cell_value = gameboard[0][row, col]
            # 2. wenn false, dann '|  '
            if cell_value == False:
                cell_string = 'c'
            
            else:
                cell_string = 'g'
            # 4. Zelle zu second_line hinzufügen
            second_line += cell_string
        # second_line ausgeben
        
        res = res + second_line + "\n"
    
    res = res[:-1]
    
    return res



def get_neighbour_count(gameboard) -> np.array:
    kernel = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]

    nc = convolve(gameboard[0].astype('int'), kernel, mode = 'wrap')
    return nc

def play(gameboard):
    neighbor_count = get_neighbour_count(gameboard)

    get_alive = np.logical_and(gameboard[0] == False, neighbor_count == 3)
    stay_alive = np.logical_and(gameboard[0] == True, np.logical_or(neighbor_count == 2, neighbor_count == 3))

    gb_a = np.logical_or(get_alive, stay_alive)

    gb = (gb_a, gameboard[1])
    return gb



def gameboard_equal(gameboard_1, gameboard_2, check_origin: bool = True):
    if gameboard_1[0].shape != gameboard_2[0].shape:
        return False
    if check_origin and gameboard_1[1] != gameboard_2[1]:
        return False
    result = np.array_equal(gameboard_1[0], gameboard_2[0])
    return result