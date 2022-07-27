from re import M
import numpy as np


x = np.full((9,9), False)

x[3,4] = True
x[4,3] = True
x[7,2] = True

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
    

print_gameboard(x)


#1. Funktion play(... definieren, in welche man ein gameboard als Attribut geben kann, und die das neue gameboard zurückgibt (NEW!)
def play(gameboard: np.array) -> np.array:
    """Macht einen Spielzug

    Args:
        gameboard (np.array): das gambeboard vor dem Spielzug

    Returns:
        np.array: das gameboard nach dem Spielzug
    """

    n = gameboard.shape[1]
    m = gameboard.shape[0]

    # 2. durch rows iterieren
    for row in range(n):
        # 3. durch cols (respektive cells) iterieren
        for col in range(m):
            # 4. Variable neighbour_count definieren (ein int) und auf 0 setzen
            neighbour = [x[n-1, m], x[n+1, m] ,x[n, m-1], x[n, m+1], x[n-1,m-1], x[n+1, m+1], x[n-1, m+1], x[n+1, m-1]]
            # 5. rund um die Zelle marschieren, und die Neighbours zählen
            neighbour_count = neighbour.count(True)
            # 6. if abfrage, um Business Logic zu implementieren (Status = True oder False) 
            if neighbour_count == 3:
                gameboard[row, col] = True

            elif neighbour_count >= 4:
                gameboard[row, col] = False
            
            elif neighbour_count <= 1:
                gameboard[row, col] = False
    
    return x




x2 = play(x)

print('x2:')
print_gameboard(x2)

x3 = play(x2)

print('x3:')
print_gameboard(x3)

