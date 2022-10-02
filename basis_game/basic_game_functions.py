import numpy as np


def create_gameboard(rows: int, cols: int) -> np.array:
    gameboard = np.full((rows,cols), False)
    return gameboard



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
    rows = gameboard.shape[0]
    cols = gameboard.shape[1]
    first_line = ' ---' * cols
    
    for row in range(rows):
        print(first_line)
        second_line = '|'
        for col in range(cols):
            # Zelle:
            # 1. Zelle in gameboard abfragen
            cell_value = gameboard[row, col]
            # 2. wenn false, dann '   |'
            if cell_value == False:
                cell_string = '   |'
            # 3. sonst: ' o |'
            else:
                cell_string = ' o |'
            # 4. Zelle zu second_line hinzufügen
            second_line += cell_string
        # second_line ausgeben
        print(second_line)
    
    print(' ---' * cols)


def play(gameboard: np.array) -> np.array:
    """Macht einen Spielzug

    Args:
        gameboard (np.array): das gambeboard vor dem Spielzug

    Returns:
        np.array: das gameboard nach dem Spielzug
    """

    rows = gameboard.shape[0]
    cols = gameboard.shape[1]

    # 1. Resultat (shallow copy, wir wollen das Input-Object nicht verändern)
    gameboard_new = gameboard.copy()
    
   
    # 2. durch rows iterieren
    for row in range(rows):
        # 3. durch cols (respektive cells) iterieren
        for col in range(cols):
            
            alive = gameboard[row, col]
            
            # 4. Die Nachbarn zählen
            
            ni = get_neighbour_indices(row, col, rows, cols)
            toprow = ni[0]
            bottomrow = ni[1]
            leftcol = ni[2]
            rightcol = ni[3]


            # wir brauche 8 neighbours. Bei N startend im Uhrzeigersinn:
            neighbour = [
                gameboard[toprow, col], # N
                gameboard[toprow, rightcol], # N-E
                gameboard[row, rightcol], # E
                gameboard[bottomrow, rightcol], # S-E
                gameboard[bottomrow, col], # S
                gameboard[bottomrow, leftcol], # S-W
                gameboard[row, leftcol], # W
                gameboard[toprow, leftcol] # N-W
            ]
            
            
            # 5. rund um die Zelle marschieren, und die Neighbours zählen
            neighbour_count = neighbour.count(True)
            # 6. if abfrage, um Business Logic zu implementieren (Status = True oder False) 
            
            if not alive:
                if neighbour_count == 3:
                    #Eine tote Zelle mit genau drei lebenden Nachbarn wird in der Folgegeneration „geboren“ (zum Leben erweckt).
                    gameboard_new[row, col] = True 
                else:
                    gameboard_new[row, col] = False

            else:
                if neighbour_count < 2:
                    #Eine lebende Zelle mit weniger als zwei lebenden Nachbarn stirbt in der Folgegeneration (an Einsamkeit).
                    gameboard_new[row, col] = False

                elif (neighbour_count == 2 or neighbour_count == 3):
                    # Eine lebende Zelle mit zwei oder drei lebenden Nachbarn bleibt in der Folgegeneration am Leben. 
                    gameboard_new[row, col] = True
            
                elif neighbour_count > 3:
                    # Eine lebende Zelle mit mehr als drei lebenden Nachbarn stirbt in der Folgegeneration (an Überbevölkerung). 
                    gameboard_new[row, col] = False
            
                

    return gameboard_new

def gameboard_equal(gameboard_1: np.array, gameboard_2: np.array):
    result = np.array_equal(gameboard_1, gameboard_2)
    return result