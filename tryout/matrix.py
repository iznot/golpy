from re import M
import numpy as np

#x = np.ndarray(shape = (6,6), dtype=bool)

x = np.full((9,9), False)

x[3,4] = True
x[4,3] = True

print(x)

def print_gameboard(gameboard : np.array):
    """Gibt das Gameboard in die Konsole aus, wie in OneNote definiert.

    Args:
        gameboard (np.array): Das Gameboard, also eine nxn Numpy Matrix mit bool
    """
    n = gameboard.shape[1]
    m = gameboard.shape[0]
    first_line = ' ---' * n
    
    for row in range(n):
        print(first_line)
        second_line = '|'
        for col in range(m):
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
    
    print(' ---' * n)
    

#    m = gameboard.shape[0]
#   first_line = '|   ' * (m + 1)
#    for i in range(m):
#        print(first_line)

print_gameboard(x)

    