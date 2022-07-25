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
    first_line = ' ---' * n
    for i in range(n):
        print(first_line)

print_gameboard(x)
