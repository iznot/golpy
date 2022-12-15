import numpy as np
import os


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



def play(gameboard) -> np.array:
    """Macht einen Spielzug

    Args:
        gameboard (np.array): das gambeboard vor dem Spielzug

    Returns:
        np.array: das gameboard nach dem Spielzug
    """

    rows = gameboard[0].shape[0]
    cols = gameboard[0].shape[1]

    # 1. Resultat (shallow copy, wir wollen das Input-Object nicht verändern)
    gameboard_new = (np.copy(gameboard[0]), gameboard[1])
    
   
    # 2. durch rows iterieren
    for row in range(rows):
        # 3. durch cols (respektive cells) iterieren
        for col in range(cols):
            
            alive = gameboard[0][row, col]
            
            # 4. Die Nachbarn zählen
            
            ni = get_neighbour_indices(row, col, rows, cols)
            toprow = ni[0]
            bottomrow = ni[1]
            leftcol = ni[2]
            rightcol = ni[3]


            # wir brauche 8 neighbours. Bei N startend im Uhrzeigersinn:
            neighbour = [
                gameboard[0][toprow, col], # N
                gameboard[0][toprow, rightcol], # N-E
                gameboard[0][row, rightcol], # E
                gameboard[0][bottomrow, rightcol], # S-E
                gameboard[0][bottomrow, col], # S
                gameboard[0][bottomrow, leftcol], # S-W
                gameboard[0][row, leftcol], # W
                gameboard[0][toprow, leftcol] # N-W
            ]
            
            
            # 5. rund um die Zelle marschieren, und die Neighbours zählen
            neighbour_count = neighbour.count(True)
            # 6. if abfrage, um Business Logic zu implementieren (Status = True oder False) 
            
            if not alive:
                if neighbour_count == 3:
                    #Eine tote Zelle mit genau drei lebenden Nachbarn wird in der Folgegeneration „geboren“ (zum Leben erweckt).
                    gameboard_new[0][row, col] = True 
                else:
                    gameboard_new[0][row, col] = False

            else:
                if neighbour_count < 2:
                    #Eine lebende Zelle mit weniger als zwei lebenden Nachbarn stirbt in der Folgegeneration (an Einsamkeit).
                    gameboard_new[0][row, col] = False

                elif (neighbour_count == 2 or neighbour_count == 3):
                    # Eine lebende Zelle mit zwei oder drei lebenden Nachbarn bleibt in der Folgegeneration am Leben. 
                    gameboard_new[0][row, col] = True
            
                elif neighbour_count > 3:
                    # Eine lebende Zelle mit mehr als drei lebenden Nachbarn stirbt in der Folgegeneration (an Überbevölkerung). 
                    gameboard_new[0][row, col] = False
            
                

    return gameboard_new

def gameboard_equal(gameboard_1, gameboard_2, check_origin: bool = True):
    if gameboard_1[0].shape != gameboard_2[0].shape:
        return False
    if check_origin and gameboard_1[1] != gameboard_2[1]:
        return False
    result = np.array_equal(gameboard_1[0], gameboard_2[0])
    return result