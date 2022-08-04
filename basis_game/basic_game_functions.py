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
            # 2. wenn false, dann '|  '
            if cell_value == False:
                cell_string = '   |'
            # 3. sonst: '| o '
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

    
    
    # 2. durch rows iterieren
    for row in range(rows):
        # 3. durch cols (respektive cells) iterieren
        for col in range(cols):
            # 4. Variable neighbour_count definieren (ein int) und auf 0 setzen
            
            ni = get_neighbour_indices(row, col, rows, cols)
            toprow = ni[0]
            bottomrow = ni[1]
            leftcol = ni[2]
            rightcol = ni[3]


            ### iznot zeugs:
            neighbour = [gameboard[toprow-1, col], gameboard[toprow+1, col], gameboard[bottomrow-1, col], gameboard[bottomrow+1, col], gameboard[row, leftcol-1], gameboard[row, leftcol+1], gameboard[row, rightcol-1], gameboard[row, rightcol+1]]
            #neighbour = [x[leftrow, col], x[rightrow, col] ,x[row, col-1], x[row, col+1], x[row-1,col-1], x[row+1, col+1], x[row-1, col+1], x[row+1, col-1]]
            # 5. rund um die Zelle marschieren, und die Neighbours zählen
            neighbour_count = neighbour.count(True)
            # 6. if abfrage, um Business Logic zu implementieren (Status = True oder False) 
            if neighbour_count == 3:
                gameboard[row, col] = True

            elif neighbour_count >= 4:
                gameboard[row, col] = False
            
            elif neighbour_count <= 1:
                gameboard[row, col] = False
            
    return gameboard

